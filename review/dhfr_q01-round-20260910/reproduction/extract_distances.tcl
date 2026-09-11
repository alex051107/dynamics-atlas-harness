# Author Figure 4 atom-pair Euclidean distances; topology-resolved ligand ID.
# Run: VMD -dispdev text -e scripts/extract_distances.tcl -args TASK_ROOT
set root [lindex $argv 0]
set outdir [file join $root derived]
file mkdir $outdir
set log [open [file join $outdir atom_mapping.tsv] w]
puts $log "system\tresid\tresname\tatom\tindex"
set info [open [file join $outdir trajectory_metadata.tsv] w]
puts $info "system\tnatoms\tnframes\tligand_resid\tligand_resname\tprotein_residues\tres28"
foreach sys {tmpp-wt tmpp-l28r d4tmpp-wt d4tmpp-l28r} {
 set psf [file join $root data ${sys}.psf]
 if {$sys eq "d4tmpp-wt"} {set psf [file join $root data d4tmpp-WT.psf]}
 set mid [mol new $psf type psf waitfor all]
 mol addfile [file join $root data ${sys}.dcd] type dcd waitfor all molid $mid
 set nf [molinfo $mid get numframes]
 set lig [atomselect $mid "name O3P O4P O5P"]
 if {[$lig num] != 3} {error "Expected three tail oxygen atoms: $sys"}
 set ligres [lsort -unique [$lig get resid]]
 set protein [atomselect $mid "protein and name CA"]
 set r28 [atomselect $mid "protein and resid 28 and name CA"]
 puts $info "$sys\t[molinfo $mid get numatoms]\t$nf\t$ligres\t[lsort -unique [$lig get resname]]\t[$protein num]\t[$r28 get resname]"
 set pairs {{18 O} {20 N} {22 O} {27 OD1} {27 OD2} {49 O} {52 NH1} {52 NH2}}
 if {[string match *l28r $sys]} {lappend pairs {28 NE} {28 NH1} {28 NH2}}
 set targetpairs {}
 foreach pair $pairs {
  lassign $pair resid atom
  set sel [atomselect $mid "protein and resid $resid and name $atom"]
  if {[$sel num]!=1} {error "Nonunique protein atom: $sys $pair"}
  set i [lindex [$sel get index] 0]
  puts $log "$sys\t$resid\t[$sel get resname]\t$atom\t$i"
  foreach oxygen {O3P O4P O5P} {
   set os [atomselect $mid "resid $ligres and name $oxygen"]
   if {[$os num]!=1} {error "Nonunique ligand atom"}
   set j [lindex [$os get index] 0]
   lappend targetpairs [list "r${resid}_${atom}_${oxygen}" $i $j]
   $os delete
  }
  $sel delete
 }
 foreach row [$lig get {resid resname name index}] {puts $log "$sys\t[join $row \t]"}
 set f [open [file join $outdir ${sys}_distances.tsv] w]
 set header [list frame_index]
 foreach pair $targetpairs {lappend header [lindex $pair 0]}
 puts $f [join $header \t]
 for {set frame 0} {$frame<$nf} {incr frame} {
  set vals [list $frame]
  foreach pair $targetpairs {
   lassign $pair label i j
   lappend vals [format %.8f [measure bond [list $i $j] molid $mid frame $frame]]
  }
  puts $f [join $vals \t]
 }
 close $f
 $lig delete; $protein delete; $r28 delete
 mol delete $mid
 puts "EXTRACTED $sys $nf frames"
}
close $log;close $info
quit
