# Source extraction only. Each XTC is paired with its own GRO.
set root [lindex $argv 0]
file mkdir "$root/derived"
foreach state {open closed} {
 set m [mol new "$root/inputs/ORADD_${state}_state.gro" type gro waitfor all]
 set sel [atomselect $m "protein and name CA"]
 set map [open "$root/derived/${state}_atom_mapping.tsv" w]
 puts $map "index\tresid\tresname\tname"
 foreach row [$sel get {index resid resname name}] {puts $map [join $row "\t"]};close $map
 animate delete all $m
 mol addfile "$root/inputs/ORADD_${state}_state_traj.xtc" type xtc waitfor all molid $m
 set out [open "$root/derived/${state}_ca_raw.tsv" w]
 set nf [molinfo $m get numframes]
 puts "SOURCE $state $nf [$sel num]"
 for {set f 0} {$f<$nf} {incr f} {
  molinfo $m set frame $f;$sel frame $f
  set row [concat [list $f] [molinfo $m get {physical_time a b c alpha beta gamma}]]
  foreach xyz [$sel get {x y z}] {set row [concat $row $xyz]}
  puts $out [join $row "\t"]
 };close $out;$sel delete;mol delete $m
}
exit
