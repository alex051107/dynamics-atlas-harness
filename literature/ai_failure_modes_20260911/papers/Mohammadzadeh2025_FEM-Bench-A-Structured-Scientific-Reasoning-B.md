# FEM-Bench: A Structured Scientific Reasoning Benchmark for Evaluating Code-Generating LLMs

**Authors:** Mohammadzadeh, Saeed; Hamdi, Erfan; Shor, Joel; Lejeune, Emma
**Year:** 2025
**Venue:** arXiv preprint
**arXiv:** 2512.20732
**Source PDF URL:** https://arxiv.org/pdf/2512.20732
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
FEM-B ENCH : A S TRUCTURED S CIENTIFIC R EASONING
B ENCHMARK FOR E VALUATING C ODE -G ENERATING LLM S

Saeed Mohammadzadeh∗
saeedmhz@bu.edu

Erfan Hamdi∗
erfan@bu.edu

Joel Shor
1. Move37 Labs
2. Department of Mechanical Engineering, Boston Univeristy
joel.shor@move37labs.ai

Emma Lejeune
elejeune@bu.edu

June 1, 2026

A BSTRACT
As LLMs advance their reasoning capabilities about the physical world, the absence of rigorous
benchmarks for evaluating their ability to generate scientiﬁcally valid physical models has become a
critical gap. Computational mechanics, the discipline that develops and applies mathematical models and numerical methods to predict the behavior of physical systems under forces, deformation,
and constraints, provides an ideal foundation for structured scientiﬁc reasoning based evaluation.
Problems follow clear mathematical structure, enforce strict physical and numerical constraints, and
support objective veriﬁcation. The discipline also requires constructing explicit models of physical
systems and reasoning about geometry, spatial relationships, and material behavior, which connects
directly to emerging goals in AI related to physical reasoning and world modeling. We introduce
FEM-Bench, a computational mechanics benchmark designed to evaluate the ability of LLMs to
generate correct ﬁnite element method (FEM) and related code. FEM-Bench 2025 contains a suite
of introductory but nontrivial tasks aligned with material from a ﬁrst graduate course on computational mechanics. These tasks capture essential numerical and physical modeling challenges while
representing only a small fraction of the complexity present in the discipline. Despite their simplicity, state-of-the-art LLMs do not reliably solve all of them. In a ﬁve attempt run, the best performing
model at function writing, Gemini 3 Pro, completed 30/33 tasks at least one out of ﬁve times, and
26/33 tasks ﬁve out of ﬁve times. The best performing model at unit test writing, GPT-5, had an
Average Joint Success Rate of 73.8%. Other popular models showed a broad range of performance
on the benchmark. FEM-Bench establishes a structured foundation for evaluating AI-generated scientiﬁc code, and future iterations will incorporate increasingly sophisticated tasks to track progress
as models evolve.
Keywords Large Language Models (LLMs) · Finite Element Method (FEM) · LLM Benchmark · Scientiﬁc Machine
Learning · Computational Mechanics · Scientiﬁc Computing · Code Generation
∗

Saeed Mohammadzadeh and Erfan Hamdi are co-ﬁrst authors

Introduction

Modern AI systems are increasingly evaluated on their ability to build internal models of the physical world, including
reasoning about forces, geometry, spatial relationships, and the mechanical behavior of physical systems [Bakhtin
et al., 2019, Wang et al., 2023]. Simultaneously, large language models (LLMs) show growing potential to assist with
scientiﬁc and engineering workﬂows, including reasoning about physical systems and automated generation of simulation and analysis code [Cui et al., 2025]. As these models advance, a central question emerges: can LLMs produce
implementations of physics-based numerical methods that are correct, reliable, and scientiﬁcally meaningful? Existing
code-generation benchmarks test general programming logic [Austin et al., 2021a, Chen et al., 2021a], software engineering skills [Jimenez et al., 2023], and mathematical reasoning [Glazer et al., 2024], but no widely used benchmarks
evaluate an LLMs ability to carry out the physical modeling, numerical discretization, and structured computational
reasoning required for advanced scientiﬁc computing [Tian et al., 2024]. Computational mechanics, the discipline
that formulates and solves mathematical models of physical systems using numerical methods, provides a natural and
rigorous domain in which to investigate these capabilities.
Computational-mechanics–based tasks represent a particularly important frontier for LLM capabilities [Jiang et al.,
2025]. Physics-based simulations grounded in this discipline underpin real-world applications in domains as diverse
as robotics [Huang et al., 2020], digital twins of aircraft and human systems [Niederer et al., 2021], climate modeling [Danabasoglu et al., 2020], and engineering design and optimization [Talischi et al., 2012]. Across these areas,
several themes are consistent: successful simulation requires the seamless integration of mathematics, physics, geometry, numerical methods, and programming, and correctness is non-negotiable. A program that runs but produces
a non-convergent, unstable, or physically impossible result is of no scientiﬁc value [Peng, 2011]. For this reason,
computational mechanics has a long and mature tradition of veriﬁcation, validation, and uncertainty quantiﬁcation
[Oberkampf and Roy, 2010], providing structured, quantitative tools for assessing whether a model is numerically
consistent, physically plausible, and predictive. These practices make the domain especially well-suited for evaluating
LLM-generated code, because failures are interpretable, quantitatively measurable, and can be traced not only to programming or structural errors but also to deeper mistakes in implementing governing equations, enforcing numerical
consistency, handling geometric transformations, or managing ﬂoating-point–sensitive operations such as numerical
integration and matrix assembly [Arndt et al., 2023, Alnæs et al., 2015].
Thus, this branch of scientiﬁc computing provides a well-structured and scientiﬁcally grounded testbed for critically
evaluating the emerging capabilities of LLMs. Problems in computational mechanics follow a precise mathematical
pipeline: e.g., governing equations are formulated, converted into weak or variational forms, discretized into ﬁnitedimensional approximations, and assembled into global algebraic systems [Courant et al., 1994, Turner et al., 1956].
Solutions are then validated through objective numerical checks such as symmetry, consistency, and mesh convergence
[Zienkiewicz and Taylor, 1997]. From the perspective of LLM reasoning, these tasks span multiple forms of structured
cognition: hierarchical reasoning in which local element routines combine into global models; geometric transformations across coordinate systems; the construction of explicit models of physical systems; and careful handling of
numerical integration, stability, and ﬂoating-point–sensitive operations. Moreover, the computational mechanics literature is extensive and mature. The computational mechanics literature spans classic textbooks [Hughes, 2003], widely
taught graduate curricula in engineering [Garikipati, 2015, Shojaei et al., 2025], and ongoing research at the frontier
of numerical methods development [Kamarei et al., 2026], offering a rich, well-understood space of problems with
clear expectations for correctness and implementation quality [Szabó and Babuška, 2021].
In this work, we introduce FEM-Bench, a benchmark designed to evaluate the ability of LLMs to generate correct
implementations of ﬁnite element method (FEM) and related computational mechanics tasks. FEM-Bench is designed
as a diagnostic challenge suite rather than a large-scale training dataset, prioritizing interpretability and reasoning depth
over task count to enable ﬁne-grained analysis of LLM failure modes in structured scientiﬁc computing. FEM-Bench
2025 focuses on introductory but nontrivial tasks aligned with material from a ﬁrst graduate course on FEM. These
tasks isolate essential numerical and physical modeling challenges while remaining amenable to automated evaluation.
Despite their relative simplicity, we ﬁnd that state-of-the-art LLMs show signiﬁcant room for improvement, revealing
signiﬁcant gaps between current model capabilities and the requirements of physics-based scientiﬁc computing.
The contributions of this paper are threefold. First, we present the FEM-Bench framework, including its design principles and scope. Second, we provide a suite of tasks and corresponding evaluation tools grounded in canonical
computational mechanics concepts. Third, we conduct a baseline evaluation across several leading LLMs to characterize current performance. Looking forward, FEM-Bench establishes a foundation for increasingly challenging
computational mechanics tasks in future iterations, enabling systematic tracking of progress in scientiﬁc computing
speciﬁc code generation.

Background

This Section provides background on computational mechanics as a domain for evaluating LLMs, emphasizing physical grounding, algorithmic structure, and rigorous veriﬁcation culture. We then motivate the need for FEM-Bench as
a benchmark designed to probe these capabilities in a scientiﬁcally meaningful setting.
2.1

Computational Mechanics as a Test of Physical World Modeling

Computational mechanics provides the mathematical and numerical foundation for simulating the behavior of physical
systems under forces, deformation, and constraints [Belytschko et al., 2014, Gurtin et al., 2010]. At its core, the ﬁeld
translates physical laws into solvable mathematical models, which are then discretized and implemented as algorithms
suitable for computation [Langtangen, 2003]. In doing so, computational mechanics serves as a direct test of whether
a model can correctly represent and reason about the physical world in algorithmic form. Among the many techniques
used in computational mechanics, the Finite Element Method (FEM) and Matrix Structural Analysis (MSA) are two
of the most widely taught and broadly applied approaches [Hughes, 2003, McGuire et al., 2000]. MSA predates FEM
and was originally developed to analyze framed structures such as trusses and beams using stiffness matrices derived
directly from structural mechanics [Argyris et al., 1960, Turner et al., 1956]. Although more specialized in scope,
MSA shares the same foundational principles as FEM–local element stiffness relations, coordinate transformations,
and global assembly–and is often viewed as an early, specialized precursor to the broader ﬁnite element framework
[Cook et al., 2007]. These shared ideas make MSA a natural companion to FEM in introductory mechanics curricula
and a relevant component of the FEM-Bench task space [Felippa, 2004].

(i) Solid mechanics problem: Given loads and boundary conditions solve for deformation
loads

Boundary
condition

Deformed
domain

Reference
domain

(ii) Discretization with the ﬁnite element method (FEM)
Nodes

Elements

Continuous domain

Discretized domain

Figure 1: Schematic overview of the ﬁnite element method (FEM). (i) A solid mechanics problem: given loads and
boundary conditions on the reference conﬁguration, solve for the deformation mapping to the deformed conﬁguration.
(ii) Discretization step: the continuous domain is approximated by a mesh of ﬁnite elements and nodes, enabling
numerical solution of the relevant governing equations.

2.2

Computational Mechanics as a Test of Structured, Multistep Reasoning

At a high level, FEM proceeds through a well-deﬁned sequence of modeling steps. Each step depends on the correct
execution of preceding stages, requiring careful composition of intermediate representations and computations. As illustrated in Fig. 1, a continuous physical domain is ﬁrst subdivided into a ﬁnite mesh of elements. Physical governing
equations are expressed in a weak or variational form, enabling approximate solutions in ﬁnite-dimensional function
spaces [Strang et al., 1973]. On each element, basis (or shape) functions deﬁne how the unknown ﬁeld varies locally,
and numerical quadrature is used to evaluate integrals appearing in the weak form [Hughes, 2003, Press, 2007]. These
element-level contributions are then assembled into a global algebraic system whose solution approximates the physical equilibrium state or transient evolution of the system [Bathe, 1996]. A schematic illustration of the discretization
appears in Fig. 1. This mathematical pipeline is central to nearly all engineering simulation software and forms the
conceptual backbone of FEM-Bench.
The mechanics tasks underlying FEM, and by extension MSA, involve several forms of structured computational reasoning that are highly relevant for evaluating modern LLMs [Tian et al., 2024]. Hierarchical reasoning is required because global behavior emerges from local element routines combined through assembly operators [Arndt et al., 2023].
Geometric reasoning appears through coordinate transformations, Jacobians, and mappings between reference and
global coordinate systems [Cottrell et al., 2009]. Numerical reasoning arises through quadrature rules, element stiffness derivations, matrix assembly, stability considerations, and ﬂoating-point–sensitive calculations [Higham, 2002].
Finally, physical reasoning is inherent to the discipline: implementations must faithfully encode conservation laws,
constitutive relations, and boundary conditions [Holzapfel, 2002]. These components appear even in introductory
FEM tasks, making the domain particularly suitable for probing LLM capabilities in scientiﬁc computing.
2.3

Veriﬁcation and Evaluation in Computational Mechanics

An essential pillar of computational mechanics, equally relevant for benchmarking, is its strong culture of veriﬁcation,
validation, and uncertainty quantiﬁcation (VVUQ) [Oberkampf and Roy, 2010]. These practices transform numerical
implementations into testable artifacts with well-deﬁned correctness criteria, making them particularly suitable for
diagnostic evaluation. Because simulation outputs must reﬂect real physical behavior, the ﬁeld has developed rigorous
practices for assessing correctness, including patch tests, equilibrium checks, symmetry requirements, energy consistency, and mesh convergence studies [Belytschko et al., 2014, Cook et al., 2007, Macneal and Harder, 1985, Roache,
1998]. These methods provide objective, quantitative signals of whether an implementation is functioning correctly.
For evaluating LLM-generated code, such tests are especially valuable: they make failures interpretable and help distinguish mistakes in programming logic [Ammann and Offutt, 2017], geometry handling [Foley, 1996], numerical
implementation [Trefethen and Bau, 2022], or ﬂoating-point–sensitive operations such as numerical integration and
matrix assembly [Higham, 2002].
2.4

Motivation for FEM-Bench

The broader landscape of existing LLM benchmarks highlights the need for a physics-based alternative. Popular codegeneration benchmarks such as HumanEval [Chen et al., 2021b], MBPP [Austin et al., 2021b], SWE-Bench [Jimenez
et al., 2024], and DS-1000 [Lai et al., 2022] evaluate programming logic, tool use, or general software engineering
skills. Datasets targeting physical reasoning often focus on qualitative judgments or simpliﬁed environments rather
than implementation of scientiﬁc algorithms [Hamdi and Lejeune, 2026, Lejeune, 2020, Shor et al., 2025]. Likewise,
benchmarks for mathematics [Hendrycks et al., 2021] or symbolic reasoning [Mirzadeh et al., 2025] do not require
translating equations into stable, reliable numerical code. The application of ﬁne-tuning open-weight models have
also been explored in multiple recent works in the ﬁeld. For example Deotale et al. Deotale et al. [2026] experimented
with ﬁne-tuning several open-weight models on a dataset of hand crafted and LLM-generated ﬁnite element codes
using FEniCS, ﬁnding that ﬁne-tuning improved model performance. Similarly, Shojaei et al. Shojaei et al. [2025]
successfully ﬁne-tuned models to develop a course-speciﬁc “expert model” integrated into the AI-University educational platform. While recent efforts like FEABench [Mudur et al., 2024] introduce agent-based tasks that interact
with professional simulation software, they primarily measure the ability to navigate complex software APIs and external tools; this highlights a critical need to decouple the interpretation of software documentation from the actual
implementation of the underlying physical and numerical reasoning. As a result, there is a limited availability of
benchmarks to evaluate whether LLMs can generate the kinds of physics-grounded, numerically consistent programs
that underpin modern scientiﬁc computing [Tian et al., 2024].
Computational mechanics therefore provides both the conceptual structure and the evaluative tools needed for such
an assessment [Oberkampf and Roy, 2010]. Its combination of mathematical rigor, geometric complexity, numerical
precision, and physical grounding makes it an ideal basis for the development of FEM-Bench [Hughes, 2003, McGuire

et al., 2000]. FEM-Bench is designed to probe four LLM capabilities that rarely co-occur in existing benchmarks and
that we revisit in detail in our error analysis (Section 4.3):
• Domain knowledge: the ability to recall sufﬁciently detailed knowledge of the underlying mechanics and
numerical structures required by a task.Evaluated by tasks in which the reference implementation must be
reproduced without scaffolding, e.g., Tier 3 (T3) variants that withhold helper functions, and standalone tasks
such as MSA_3D_local_geometric_stiffness.
• Compositional reasoning: the ability to combine and manipulate multiple components into a correct multistep computation. Evaluated through the tiered helper-function design (T1/T2/T3) and through tasks such as
MSA_3D_elastic_critical_load, whose reference implementation chains together multiple physical steps
(Fig. 4).
• Algorithmic ﬁdelity: the ability to implement a computation with the consistency required for it to execute
and produce numerically correct outputs (correct indexing, consistent sign conventions, complete routines,
etc.). Evaluated by reference-output matching on curated veriﬁcation inputs (Section 3.6.1).
• Self-veriﬁcation: the ability to express the correctness criteria of a task as discriminative, physics-aware unit
tests that both pass on a correct implementation and fail on known-incorrect implementations. Evaluated by
the joint test success rate over expected-failure cases (Section 3.6.2).
In the next Section, we introduce the benchmark design and describe the task suite that forms the FEM-Bench 2025
release.

Methods

This Section describes the FEM-Bench methodology, including the structure of the benchmark, the construction of
tasks and prompts, the evaluation pipeline for code and test generation, and the initial selection of LLMs to evaluate.
FEM-Bench follows a modular design: tasks are deﬁned as self-contained Python modules, prompts are generated
automatically from task metadata, LLM outputs are parsed and validated, and results are computed through referencebased numerical and unit-testing procedures. The framework is designed for reproducibility, extensibility, and principled evaluation. A high-level overview of the FEM-Bench workﬂow, including task loading, prompt generation,
model inference, and evaluation, is shown in Fig. 2, with the corresponding pseudocode provided in Algorithm 1.
Algorithm 1 FEM-Bench Evaluation Pipeline
Input: Tasks T , models M
Output: Function Correctness score, Average joint test success rate
1: Load tasks
2: Generate task and test prompts
3: for all model m ∈ M do
4:
for all task t ∈ T do
5:
Generate code with m using task prompt of t
6:
Generate tests with m using test prompt of t
7:
end for
8: end for
9: Evaluate generated code against reference outputs
10: Evaluate generated tests on reference function and expected-failure implementations
11: Aggregate and save scores

3.1

Problem Deﬁnition

FEM-Bench evaluates two complementary capabilities of LLMs: the ability to generate numerically correct scientiﬁc
code, and the ability to generate unit tests that verify that code. In this benchmark, producing correct code means
generating a Python function that conforms to a prescribed signature, runs without syntax errors, and returns outputs
that satisfy the mathematical and physical requirements of the task. Similarly, producing a correct unit test means
generating tests written using pytest, a widely used Python testing framework, that execute without errors, pass
on the reference implementation, and fail on a curated set of known incorrect implementations. Because scientiﬁc
software correctness depends as much on veriﬁcation as on implementation, FEM-Bench treats code synthesis and test
synthesis as intertwined, ﬁrst-class components of the benchmark. Together, these two components deﬁne the core

Figure 2: Overview of the FEM-Bench workﬂow. Tasks are deﬁned as self-contained Python modules specifying
reference implementations, dependencies, and unit tests. The core FEM-Bench software loads these tasks, constructs
standardized prompts for both code-generation and test-generation, and interfaces with LLMs through model-speciﬁc
API clients. LLM outputs (generated code and test suites) are then parsed, validated, and evaluated using referencebased numerical checks and expected-failure unit tests. The framework produces detailed scores for each model and
task, enabling reproducible and interpretable comparison of LLM performance.
problem that FEM-Bench poses to LLMs: not simply producing code that runs, but producing code and unit tests that
are technically correct.
3.2

Task Deﬁnition and Structure

FEM-Bench deﬁnes each task as a self-contained Python module with a standardized, explicit structure designed for
transparency, reproducibility, and extensibility. With regard to scientiﬁc content, each task centers around a single
Python function with a prescribed signature that computes a well-deﬁned numerical or physical quantity. For example,
the core content of a task may involve computing a local element stiffness matrix, evaluating shape functions and their
derivatives, assembling a global stiffness matrix, or running a full analysis from start to ﬁnish. Within a given task,
the goal will be to implement and test the prescribed core content. For core content where the typical implementation
would involve many helper functions, such as elastic critical load analysis, which requires a linear elastic solve, geometric stiffness assembly, and a generalized eigenvalue solve, we often deﬁne separate tasks corresponding to different
tiers of provided helper functions. This tiering system is the primary mechanism by which FEM-Bench modulates task
difﬁculty and isolates speciﬁc reasoning demands. A “higher-level” task such as elastic_critical_load can then
be evaluated with varying amounts of scaffolding, exposing whether a model’s failure stems from either a speciﬁc
sub-component, or compositional reasoning across components. Unit tests, also contained within each task, are designed to probe correctness at multiple levels, including structural properties, consistency with sub-components, and
agreement with analytical solutions. A task is considered complete when its unit tests collectively cover the most
meaningful physical and numerical failure modes, as illustrated by the expected-failure implementations bundled with
each task.
Every task includes: a reference implementation with a detailed docstring (which becomes part of the LLM prompt)
specifying mathematical and physical requirements, Pytest-style test functions with descriptive docstrings (also incorporated directly into the prompt), optional dependency functions, known incorrect implementations used as expected
failures, and a single task_info() function. The task_info() function assembles these components into a structured
dictionary that contains all metadata and source code required for prompt generation, execution, and evaluation. This
“source-ﬁrst” design ensures that tasks remain fully executable and easy to inspect or extend. The full task template is
shown in Listing 1.

All tasks in FEM-Bench 2025 are manually written by the authors, with LLM assistance limited to narrow sub-function
contributions that were reviewed and veriﬁed. Each task begins from a working codebase developed via test-driven
development and validated against multiple analytical solutions.
Listing 1: FEM-Bench task template
import numpy as np
# === Dependency functions ( if any ) ===
def helper_1 (...) :
def helper_2 (...) :
# === Reference implementation ===
def main_fcn (...) :
" " " Compute or solve something . " " "
# === Test functions ===
def test_case_1 ( fcn ):
" " " Docstring explaining what is tested . " " "
# === Known failing examples ( optional ) ===
def fail_case_1 (...) :
def fail_case_2 (...) :
# === task_info () metadata ===
def task_info () :
task_id = " unique_task_name "
task_short_description = " concise description of what the task does "
created_date = " YYYY - MM - DD "
created_by = " your_name "
main_fcn = main_fcn
required_imports = [
" import numpy as np " ,
" import pytest " ,
# additional imports if needed
fcn_dependencies = [ helper_1 , helper_2 ]

# or [] if none

reference_verification_inputs = [
# List of lists : each sublist contains args for main_fcn
[ arg1 , arg2 , ...] ,
test_cases = [
{
" test_code " : test_case_1 ,
" expected_failures " : [ fail_case_1 , fail_case_2 ]
},
return {
" task_id " : task_id ,
" task_short_description " : task_short_description ,
" created_date " : created_date ,
" created_by " : created_by ,

# or []

" main_fcn " : main_fcn ,
" required_imports " : required_imports ,
" fcn_dependencies " : fcn_dependencies ,
" reference_verification_inputs " : reference_verification_inputs ,
" test_cases " : test_cases ,
" allow_negation_for_match " : False ,
" python_version ": " version_number " ,
" package_versions " : { " numpy " : " version " },
}

When a task is loaded, FEM-Bench extracts and normalizes the source code for the reference function, helpers, and
tests, and stores them in a Task object deﬁned in task_base.py. This object provides the canonical representation of
the task throughout the remainder of the pipeline, including prompt construction, LLM inference, and evaluation.
3.2.1

Example Task

To ground this template in a concrete example, Listing 2 shows an actual FEM-Bench task from the FEM-Bench
2025 suite. This task deﬁnes the local 12 × 12 elastic stiffness matrix for a 3D Euler–Bernoulli beam element,
along with two pytest-style test functions. The ﬁrst test (test_local_stiffness_3D_beam) checks structural
properties such as symmetry, rigidity, and consistency of axial, torsional, and bending terms. The second test
(test_cantilever_deflection_matches_euler_bernoulli) compares numerical displacements with closed-form
Euler–Bernoulli beam theory under different loading directions. The task_info() function then packages the reference implementation, veriﬁcation inputs, and expected-failure implementations into the standardized FEM-Bench task
format. Supplementary examples of test cases and expected failure functions are shown in Appendix C, in Table 7 and
8 respectively. All complete task implementations used in this study are published on the FEM-Bench GitHub.
Listing 2: Example FEM-Bench task: local stiffness matrix for a 3D Euler–Bernoulli beam element.
import numpy as np

def MSA_3D_local_elastic_stiffness_CC0_H0_T0 (
Return the 12 x12 local elastic stiffness matrix for a 3 D Euler - Bernoulli beam
element .
The beam is assumed to be aligned with the local x - axis . The stiffness matrix
relates local nodal displacements and rotations to forces and moments using the
equation :
[ force_vector ] = [ stiffness_matrix ] @ [ displacement_vector ]
Degrees of freedom are ordered as :
[ u1 , v1 , w1 , x1 , y1 , z1 , u2 , v2 , w2 , x2 , y2 , z2 ]
Where :
- u , v , w : displacements along local x , y , z
- x , y , z : rotations about local x , y , z
- Subscripts 1 and 2 refer to node i and node j of the element
Parameters :
E ( float ) : Young ’s modulus
nu ( float ) : Poisson ’s ratio ( used for torsion only )
A ( float ) : Cross - sectional area

L ( float ) : Length of the beam element
Iy ( float ) : Second moment of area about the local y - axis
Iz ( float ) : Second moment of area about the local z - axis
J ( float ) : Torsional constant
Returns :
np . ndarray : A 12 x12 symmetric stiffness matrix representing axial , torsional ,
and bending stiffness in local coordinates .
k_e = np . zeros ((12 , 12) )
# Axial terms - extension of local x axis
axial_stiffness = E * A / L
k_e [0 , 0] = axial_stiffness
k_e [0 , 6] = - axial_stiffness
k_e [6 , 0] = - axial_stiffness
k_e [6 , 6] = axial_stiffness
# Torsion terms - rotation about local x axis
torsional_stiffness = E * J / (2.0 * (1 + nu ) * L)
k_e [3 , 3] = torsional_stiffness
k_e [3 , 9] = - torsional_stiffness
k_e [9 , 3] = - torsional_stiffness
k_e [9 , 9] = torsional_stiffness
# Bending terms - bending about local z axis
k_e [1 , 1] = E * 12.0 * Iz / L ** 3.0
k_e [1 , 7] = E * -12.0 * Iz / L ** 3.0
k_e [7 , 1] = E * -12.0 * Iz / L ** 3.0
k_e [7 , 7] = E * 12.0 * Iz / L ** 3.0
k_e [1 , 5] = E * 6.0 * Iz / L ** 2.0
k_e [5 , 1] = E * 6.0 * Iz / L ** 2.0
k_e [1 , 11] = E * 6.0 * Iz / L ** 2.0
k_e [11 , 1] = E * 6.0 * Iz / L ** 2.0
k_e [5 , 7] = E * -6.0 * Iz / L ** 2.0
k_e [7 , 5] = E * -6.0 * Iz / L ** 2.0
k_e [7 , 11] = E * -6.0 * Iz / L ** 2.0
k_e [11 , 7] = E * -6.0 * Iz / L ** 2.0
k_e [5 , 5] = E * 4.0 * Iz / L
k_e [11 , 11] = E * 4.0 * Iz / L
k_e [5 , 11] = E * 2.0 * Iz / L
k_e [11 , 5] = E * 2.0 * Iz / L
# Bending terms - bending about local y axis
k_e [2 , 2] = E * 12.0 * Iy / L ** 3.0
k_e [2 , 8] = E * -12.0 * Iy / L ** 3.0
k_e [8 , 2] = E * -12.0 * Iy / L ** 3.0
k_e [8 , 8] = E * 12.0 * Iy / L ** 3.0
k_e [2 , 4] = E * -6.0 * Iy / L ** 2.0
k_e [4 , 2] = E * -6.0 * Iy / L ** 2.0
k_e [2 , 10] = E * -6.0 * Iy / L ** 2.0
k_e [10 , 2] = E * -6.0 * Iy / L ** 2.0
k_e [4 , 8] = E * 6.0 * Iy / L ** 2.0
k_e [8 , 4] = E * 6.0 * Iy / L ** 2.0
k_e [8 , 10] = E * 6.0 * Iy / L ** 2.0
k_e [10 , 8] = E * 6.0 * Iy / L ** 2.0
k_e [4 , 4] = E * 4.0 * Iy / L
k_e [10 , 10] = E * 4.0 * Iy / L
k_e [4 , 10] = E * 2.0 * Iy / L
k_e [10 , 4] = E * 2.0 * Iy / L
return k_e

def test_local_stiffness_3D_beam ( fcn ):
Comprehensive test for local_elastic_stiffness_matrix_3D_beam :
- shape check
- symmetry
- expected singularity due to rigid body modes

- block - level verification of axial , torsion , and bending terms
# Beam properties
E = 200 e9
# Young ’s modulus
nu = 0.3
# Poisson ’s ratio
A = 0.01
# Cross - sectional area
L = 2.0
# Length of the beam
Iy = 8
# Moment of inertia about y
Iz = 6
# Moment of inertia about z
J = 1
# Torsional constant
k = fcn (E , nu , A , L , Iy , Iz , J)
# --- Shape check --assert k. shape == (12 , 12)
# --- Symmetry check --assert np . allclose (k , k.T , atol =1e -12)
# --- Singularity check ( due to 6 rigid - body modes ) --eigvals = np . linalg . eigvalsh (k)
min_eigval = np . min ( np . abs ( eigvals ))
assert min_eigval < 1e -10 , f " Expected a zero eigenvalue , but smallest was {
min_eigval :.2 e} "
# --- Axial terms block --expected_axial = E * A / L
assert np . isclose (k [0 , 0] , expected_axial , rtol =1e -12)
assert np . isclose (k [0 , 6] , - expected_axial , rtol =1e -12)
assert np . isclose (k [6 , 0] , - expected_axial , rtol =1e -12)
assert np . isclose (k [6 , 6] , expected_axial , rtol =1e -12)
# --- Torsional terms block ( theta_x DOFs ) --G = E / (2 * (1 + nu ))
expected_torsion = G * J / L
assert np . isclose (k [3 , 3] , expected_torsion , rtol =1e -12)
assert np . isclose (k [3 , 9] , - expected_torsion , rtol =1e -12)
assert np . isclose (k [9 , 3] , - expected_torsion , rtol =1e -12)
assert np . isclose (k [9 , 9] , expected_torsion , rtol =1e -12)
# --- Bending about local z (v -- theta_z : DOFs 1, 5, 7, 11) --expected_bz_11 = E * 12.0 * Iz / L **3
expected_bz_15 = E * 6.0 * Iz / L **2
expected_bz_55 = E * 4.0 * Iz / L
expected_bz_511 = E * 2.0 * Iz / L
assert np . isclose (k [1 , 1] , expected_bz_11 , rtol =1e -12)
assert np . isclose (k [1 , 5] , expected_bz_15 , rtol =1e -12)
assert np . isclose (k [5 , 5] , expected_bz_55 , rtol =1e -12)
assert np . isclose (k [5 , 11] , expected_bz_511 , rtol =1e -12)
# --- Bending about local y (w -- theta_y : DOFs 2, 4, 8, 10) --expected_by_22 = E * 12.0 * Iy / L **3
expected_by_24 = -E * 6.0 * Iy / L **2
expected_by_44 = E * 4.0 * Iy / L
expected_by_410 = E * 2.0 * Iy / L
assert np . isclose (k [2 , 2] , expected_by_22 , rtol =1e -12)
assert np . isclose (k [2 , 4] , expected_by_24 , rtol =1e -12)
assert np . isclose (k [4 , 4] , expected_by_44 , rtol =1e -12)
assert np . isclose (k [4 , 10] , expected_by_410 , rtol =1e -12)

def test_cantilever_deflection_matches_euler_bernoulli ( fcn ):

Apply a perpendicular point load in the z direction to the tip of a cantilever
beam and verify that the computed displacement matches the analytical solution
from Euler - Bernoulli beam theory .
Apply a perpendicular point load in the y direction to the tip of a cantilever
beam and verify that the computed displacement matches the analytical solution
from Euler - Bernoulli beam theory .
Apply a parallel point load in the x direction to the tip of a cantilever beam and
verify that the computed displacement matches the analytical solution from
Euler - Bernoulli beam theory .
E = 210 e6
# Young ’s modulus ( Pa )
nu = 0.3
A = 0.01
# Cross - sectional area ( m ^2)
L = 2.0
# Beam length ( m )
Iy = 4e -2
# Bending about y
Iz = 6e -2
# Bending about z
J = 1e -2
# Torsion
F_applied = -100.0

# Applied load ( N )

# Build stiffness matrix
K = fcn (E , nu , A , L , Iy , Iz , J)
# z direction loading :
# Apply load at node 2 in local z - direction ( DOF 8)
f_ext [8] = F_applied
delta_z = u_f [2]
# DOF 8 - z displacement
delta_expected = F_applied * L **3 / (3 * E * Iy )
assert np . isclose ( delta_z , delta_expected , rtol =1e -9)
# y direction loading :
# Apply load at node 2 in local y - direction ( DOF 7)
f_ext [7] = F_applied
delta_y = u_f [1]
# DOF 7 - y displacement
delta_expected = F_applied * L **3 / (3 * E * Iz )
assert np . isclose ( delta_y , delta_expected , rtol =1e -9)
# x direction loading :
# Apply load at node 2 in local x - direction ( DOF 6)
f_ext [6] = F_applied
delta_x = u_f [0]
# DOF 6 - x displacement
delta_expected = F_applied * L / (E * A )
assert np . isclose ( delta_x , delta_expected , rtol =1e -9)

def local_elastic_stiffness_matrix_3D_beam_flipped_Iz_Iy (

k_e = np . zeros ((12 , 12) )
# Axial terms - extension of local x axis
axial_stiffness = E * A / L
k_e [0 , 0] = axial_stiffness
k_e [0 , 6] = - axial_stiffness
k_e [6 , 0] = - axial_stiffness
k_e [6 , 6] = axial_stiffness
# Torsion terms - rotation about local x axis
torsional_stiffness = E * J / (2.0 * (1 + nu ) * L)
k_e [3 , 3] = torsional_stiffness
k_e [3 , 9] = - torsional_stiffness
k_e [9 , 3] = - torsional_stiffness
k_e [9 , 9] = torsional_stiffness
# Bending terms - bending about local z axis
k_e [1 , 1] = E * 12.0 * Iy / L ** 3.0
k_e [1 , 7] = E * -12.0 * Iy / L ** 3.0
k_e [7 , 1] = E * -12.0 * Iy / L ** 3.0
k_e [7 , 7] = E * 12.0 * Iy / L ** 3.0
k_e [1 , 5] = E * 6.0 * Iy / L ** 2.0
k_e [5 , 1] = E * 6.0 * Iy / L ** 2.0
k_e [1 , 11] = E * 6.0 * Iy / L ** 2.0
k_e [11 , 1] = E * 6.0 * Iy / L ** 2.0
k_e [5 , 7] = E * -6.0 * Iy / L ** 2.0
k_e [7 , 5] = E * -6.0 * Iy / L ** 2.0
k_e [7 , 11] = E * -6.0 * Iy / L ** 2.0
k_e [11 , 7] = E * -6.0 * Iy / L ** 2.0
k_e [5 , 5] = E * 4.0 * Iy / L
k_e [11 , 11] = E * 4.0 * Iy / L
k_e [5 , 11] = E * 2.0 * Iy / L
k_e [11 , 5] = E * 2.0 * Iy / L
# Bending terms - bending about local y axis
k_e [2 , 2] = E * 12.0 * Iz / L ** 3.0
k_e [2 , 8] = E * -12.0 * Iz / L ** 3.0
k_e [8 , 2] = E * -12.0 * Iz / L ** 3.0
k_e [8 , 8] = E * 12.0 * Iz / L ** 3.0
k_e [2 , 4] = E * -6.0 * Iz / L ** 2.0
k_e [4 , 2] = E * -6.0 * Iz / L ** 2.0
k_e [2 , 10] = E * -6.0 * Iz / L ** 2.0
k_e [10 , 2] = E * -6.0 * Iz / L ** 2.0
k_e [4 , 8] = E * 6.0 * Iz / L ** 2.0
k_e [8 , 4] = E * 6.0 * Iz / L ** 2.0
k_e [8 , 10] = E * 6.0 * Iz / L ** 2.0
k_e [10 , 8] = E * 6.0 * Iz / L ** 2.0
k_e [4 , 4] = E * 4.0 * Iz / L
k_e [10 , 10] = E * 4.0 * Iz / L
k_e [4 , 10] = E * 2.0 * Iz / L
k_e [10 , 4] = E * 2.0 * Iz / L
return k_e

def all_random (
return np . random . random ((12 , 12) )

def task_info () :
task_id = " MSA_3D_local_elastic_stiffness_CC0_H0_T0 "
task_short_description = " creates an element stiffness matrix for a 3 D beam "
created_date = " 2025 -07 -31 "
created_by = " elejeune11 "
main_fcn = MSA_3D_local_elastic_stiffness_CC0_H0_T0
required_imports = [" import numpy as np " , " import pytest " , " from typing import
Callable " ]
fcn_dependencies = []
reference_verification_inputs = [[100 , 0.3 , 10 , 5, 30 , 25 , 10] ,
[10000 , 0.4 , 77 , 55 , 300 , 250 , 9.9] ,
[98000 , 0.3 , 5.5 , 55 , 300 , 250 , 9.4] ,
[6790 , 0.2 , 10.6 , 4.7 , 44 , 34 , 20.1] ,]
test_cases = [{ " test_code " : test_local_stiffness_3D_beam , " expected_failures " : [
local_elastic_stiffness_matrix_3D_beam_flipped_Iz_Iy ]} ,
{ " test_code " : test_cantilever_deflection_matches_euler_bernoulli , "
expected_failures " : [ all_random ,
local_elastic_stiffness_matrix_3D_beam_flipped_Iz_Iy ]}]
return {
" task_id " : task_id ,
" task_short_description " : task_short_description ,
" created_date " : created_date ,
" created_by " : created_by ,
" main_fcn " : main_fcn ,
" required_imports " : required_imports ,
" fcn_dependencies " : fcn_dependencies ,
" reference_verification_inputs " : reference_verification_inputs ,
" test_cases " : test_cases ,
}

This example task illustrates how FEM-Bench packages a conceptually simple numerical routine, namely a closedform expression for the 12×12 local stiffness matrix of a 3D Euler–Bernoulli beam, into a fully testable benchmarking
unit. Although the reference implementation itself is straightforward, the accompanying tests probe whether an LLM
can correctly encode essential physical and numerical properties such as symmetry, rigid-body modes, consistency
of bending, torsional, and axial sub-blocks, and analytical veriﬁcation. These unit tests elevate the task from mere
formula transcription to a richer assessment of mathematical understanding, geometric reasoning, and the ability to
operationalize core principles of computational mechanics in executable code. Notably, this is one of the simplest
tasks in FEM-Bench 2025.
3.3

Prompt Generation

Given a Task object, FEM-Bench constructs two prompts: one for code generation and one for test generation. Both
prompts are produced by inserting task-speciﬁc information, such as the function signature, docstring, allowed imports, and any dependency functions, into standardized templates stored in the prompt_templates/ directory. These
templates provide explicit instructions about how the model must format its output and deﬁne strict constraints to
ensure that the result is valid, executable Python.
Prompts are generated using task_to_code_prompt and task_to_test_prompt, and are saved to disk prior to model
inference to ensure reproducibility and to support debugging. The code-generation prompt integrates the function
signature, docstring, and task-speciﬁc dependencies into a ﬁxed textual template. This template is shown in Listing 3.
Listing 3: FEM-Bench code-generation prompt template
# Python Function Implementation Task
Write a Python function that matches the exact signature and docstring provided below .
# # Requirements :
- Keep the function name , parameter names , and docstring exactly as shown
- Do not add any code outside the function definition
{% if task . required_imports %}

- Use only the following imports :
{{ task . required_imports | join ( ’\ n ’) }}
{% else %}
- No imports are available
- You may call only the helper functions listed below - their full implementations are
provided
- Do not re - implement or modify them
- Output only valid Python code ( no explanations , comments , or markdown )
- Implement the functionality as described in the docstring
{% if task . python_version or task . package_versions %}
# # Environment Specifications :
{% if task . python_version -%}
- Python Version : {{ task . python_version }}
{% - if task . package_versions -%}
- Package Versions :
{% for package , version in task . package_versions . items () %}
version }}

- {{ package }}: {{

# # Available Helper Functions :
{% if task . fcn_dependency_code -%}
{{ task . fcn_dependency_code | map ( ’ dedent ’) | join ( ’\ n \ n ’) }}
{% - else -%}
( None )
##
##
{{
{{

Function Signature :
Only complete the function below :
signature }}
docstring }}

# Output :
# Only return the complete Python function - no extra text , explanation , or formatting
.

A corresponding test-generation prompt is constructed for each task. This prompt includes the function to be tested,
the names and descriptions of the pytest-style test functions to be written, and the rules governing the structure and
validity of the resulting tests. The test-generation template is shown in Listing 4.
Listing 4: FEM-Bench test-generation prompt template
# Python Task : Write Pytest Tests for a Function
Below is the function you are testing . Use its signature and docstring to understand
its behavior .
# # Only complete the test functions below :
{{ signature }}
{{ docstring }}
# # Your Goal :
Write pytest - style test functions that verify the correctness of the function above .
# # Requirements :
- Use the exact test function names listed below
- Each test must accept a single argument : ‘fcn ‘ - the function to test
- Use ‘ assert ‘ statements to check correctness
- Each test must include a descriptive docstring

- Do not include print statements , logging , or example usage
- Output only valid Python code - no explanations , markdown , or comments
{% if task . python_version or task . package_versions %}
# # Environment Specifications :
{% if task . python_version -%}
- Python Version : {{ task . python_version }}
{% if task . package_versions -%}
- Package Versions :
{% for package , version in task . package_versions . items () %}
version }}

- {{ package }}: {{

# # Test Functions to Implement :
{% if test_cases %}
{% for test in test_cases %}
- {{ test . name }}: " {{ test . doc }} "
{% else %}
- ( no test cases found )
# Output :
# Only return valid pytest test functions - no prose , markdown , or commentary .

Because each prompt includes the docstrings taken directly from the task deﬁnition, the docstrings plays a central
role in guiding LLM behavior. In practice, they provide the primary description of the mathematical and numerical
requirements of the task, making it one of the most inﬂuential components of the overall prompt.
3.4

Prompting Procedure and Inference Settings

FEM-Bench queries each model through a uniﬁed interface that wraps provider-speciﬁc API clients contained in the
llm_api/ directory. All prompts are saved to disk before inference to ensure reproducibility. For each task and model,
FEM-Bench requests exactly one code-generation completion and one test-generation completion. By default, all calls
use the following settings: temperature is set to 0.1 consistent with common practice in the LLM code-generation
literature and within the low-temperature range recommended by providers for analytical and code-generation tasks.,
the thinking/reasoning level is set to “high” for models that support this parameter (i.e., Gemini 3 Pro, GPT-5, and
GPT-5 mini), and no system prompt is applied unless explicitly speciﬁed (see Appendix D). The inference setting used
for each model are listed in Table 6.
The prompt templates were reﬁned iteratively with the goal of not limiting model performance through poor prompt
construction. As shown in listings 3 and 4, both templates include explicit output format constraints, import restrictions, helper function availability, and environment speciﬁcations, providing models with all information necessary
to succeed while constraining outputs to valid, executable Python. This design was validated by the GEPA prompt
optimization experiments described in Appendix D, which found no generic prompt improvements and conﬁrmed that
meaningful performance gains required injecting task-speciﬁc domain knowledge rather than generic reasoning instructions. Observed performance differences across models and tasks therefore reﬂect genuine capability differences
rather than prompt-induced artifacts.
The dispatcher functions call_llm_for_code() and call_llm_for_tests() forward prompts to the appropriate
backend (OpenAI, Gemini, Claude, or Together AI for open-source LLama and Qwen models). Each provider
is queried through its native API: OpenAI models use the Chat Completions interface, Gemini models use the
google.genai client, Claude models use the Anthropic Messages API, and open-source LLaMA and Qwen models are accessed via Together AI platform. A model-speciﬁc token policy sets the maximum output length, and all
clients implement retry logic with exponential backoff. Each task is evaluated via an independent API call with no
shared context or memory across tasks, ensuring that model outputs for one task cannot inﬂuence outputs for another.
Raw responses are cleaned using utilities in clean_utils.py, which remove code fences and extraneous text before
extracting either a single function deﬁnition or a set of pytest-style test functions. Outputs that are empty, unparsable, or

syntactically invalid are marked as incorrect. These inference settings provide consistent and reproducible evaluation
across models despite differences in provider APIs.
3.5

Output Parsing and Validation

LLM outputs are parsed and validated using a set of strict rules designed to ensure clean and consistent evaluation.
Each completion must contain syntactically valid Python, veriﬁed with ast.parse(). Only the ﬁrst function deﬁnition
in the output is extracted and evaluated, and any imports not explicitly listed in the task speciﬁcation cause the attempt
to fail. For test-generation tasks, the output must deﬁne at least one function whose name begins with test_; outputs
missing such functions receive a score of zero.
3.6

Evaluation of Generated Code and Tests

FEM-Bench evaluates the correctness of both generated implementations and generated test suites using a controlled
execution pipeline that combines numerical comparison, structured test logic, and isolated runtime environments.
After parsing model outputs, the benchmark reconstructs an executable namespace by combining the generated code
with the allowed imports and any task-speciﬁed dependency functions, as implemented in evaluate_output.py and
executed through the pipeline in pipeline_utils.py. If execution raises a runtime error, the attempt is immediately
marked as incorrect. For functions that execute successfully, numerical correctness is assessed by comparing their
outputs to those of the reference implementation using a recursive matching procedure that supports scalars, arrays,
dictionaries, and nested data structures within speciﬁed numerical tolerances. This procedure traverses the output
structure type by type, applying numerical tolerances to scalars and arrays, recursing into lists, tuples, and dictionary
values, and returning false at the ﬁrst mismatch encountered at any level of the hierarchy. Together, these validation
steps ensure that irrelevant text, syntactic irregularities, or execution failures do not compromise the reliability of the
evaluation.
3.6.1

Function Correctness Evaluation

To evaluate implementation correctness, FEM-Bench executes the LLM generated function on a curated set of veriﬁcation inputs speciﬁed in the task deﬁnition. For each input, FEM-Bench computes the corresponding reference output
and compares it to the LLM-generated output using the utility _values_match, which performs recursive numerical matching over scalars, NumPy arrays, dictionaries, and nested Python structures within a conﬁgurable tolerance.
Runtime errors during execution also result in failure.
The correctness metric is binary and deﬁned as:
{
1 (or 3), if all veriﬁcation inputs match reference outputs within tolerance,
Correctness =
0 (or 7), otherwise.

(1)

For interpretability, FEM-Bench stores detailed comparison logs, including reference outputs, generated outputs, and
any raised exceptions, as JSON ﬁles in the results directory.
3.6.2

Test-Suite Evaluation

Test-generation evaluation proceeds in three stages. First, FEM-Bench loads the reference implementation and executes each generated test function against it. A test must pass on the reference implementation to be considered valid.
Second, FEM-Bench executes each test against all expected failure implementations provided with the task. A test
must fail on every expected-failure implementation in order to receive credit for failure detection. Third, joint success
is computed by checking that a test both passes the reference implementation and fails on all expected failures. These
checks are performed using evaluate_task_tests(), which loads test functions, handles dependency imports, and
executes each test in a protected namespace while capturing exceptions through pytest. The ﬁnal test-suite score for a
model is the percentage of tests achieving joint success.
3.6.3

Aggregate Metrics

After evaluating all functions and test suites for all tasks and models, FEM-Bench computes four aggregate metrics
for each model: the percentage of function implementations whose outputs match the reference implementation; the
average percentage of generated tests that pass on the reference implementation; the average percentage of expectedfailure cases that are correctly detected; and the average joint success rate, deﬁned as the percentage of tests that
both pass on the reference and fail on all expected failures. Brieﬂy, each task includes one or more expected failure

implementations, manually written known-incorrect functions that a well-designed unit test should reliably detect.
These fall into several interpretable categories: formula errors (e.g., swapping Iy and Iz in bending terms), sign or
ordering errors (e.g., incorrect cross-product order in a coordinate transformation), missing physics (e.g., terms from a
geometric stiffness matrix), missing numerical checks (e.g., solving a linear system without ill-conditioning detection),
and trivially wrong outputs (e.g., returning a random matrix). Ensuring failure on the know expected failures makes
the joint test success a meaningful check, rather than an incidental property of the output. In Appendix C, Table 8,
we provide a few examples of expected failures and point the reader to the FEM-Bench GitHub page for access to
the full suite. These metrics are computed using compute_aggregate_score() and written to disk in both JSON and
Markdown summary formats for analysis and comparison.
3.7

FEM-Bench 2025 Task Suite

The FEM-Bench 2025 release contains a curated set of introductory but nontrivial tasks drawn from standard introductory computational mechanics curricula. The suite spans three major domains: one-dimensional ﬁnite element
methods (FEM 1D), two-dimensional ﬁnite element methods (FEM 2D), and three-dimensional matrix structural analysis (MSA 3D). Across these domains, tasks assess element-level routines, mesh generation, quadrature, geometric
mappings, stiffness and load assembly, coordinate transformations, and linear and eigenvalue solves.
Although FEM-Bench 2025 comprises only 33 tasks, it is designed as a diagnostic challenge suite rather than a largescale training dataset. Each task is dense, multi-step, and algorithmically structured, typically requiring the correct
integration of multiple interdependent computational components in a single solution, along with the synthesis of unit
tests that encode the physical, numerical, and algorithmic constraints of the problem. As with other diagnostic benchmarks, FEM-Bench prioritizes interpretability and reasoning depth over task count, enabling ﬁne-grained analysis of
failure modes in structured scientiﬁc computing.
Each task is classiﬁed using a CC/H/T identiﬁer, where CC indicates the conceptual challenge level (CC0 for linearelastic and basic discretization tasks, CC1 for elastic critical-load analysis), H denotes the number of helper functions
used in the reference implementation, and T denotes which of these helper functions are provided to the model (T0:
none needed, none provided; T1: all provided; T2: subset provided; T3: none provided despite being used in the
reference). This classiﬁcation enables systematic evaluation of how LLMs handle increasing levels of functional
decomposition, abstraction, and reasoning complexity. The tiers are designed to isolate domain knowledge deﬁcits (the
model cannot construct a missing component) from compositional reasoning deﬁcits (the model has all components
but cannot chain them). Tasks with the deepest functional decomposition – such as elastic critical load analysis – are
evaluated at multiple tiers so we can observe how performance changes as helpers are added. Simpler tasks that would
traditionally be implemented without helper functions appear only at T0, since there is nothing to vary. This structure
underpins the error analysis in Section 4.3 A full list of tasks is provided in Table 1.
Looking forward, we anticipate expanding the FEM-Bench suite to include additional tasks and domains. The FEMBench 2025 task suite is released fully open access to enable reproducibility and community contribution. However,
to mitigate the risk of data leakage and overﬁtting as LLM training corpora evolve, not all future tasks may be publicly
released. Subsequent iterations will therefore likely withhold a portion of the task suite from public release to preserve
benchmark integrity, while keeping the design principles, task structure, and evaluation methodology fully transparent.
In this sense, FEM-Bench 2025 is intended not only as a benchmark, but also as a representative demonstration of the
typical structure, complexity, and reasoning demands of computational mechanics tasks, enabling future evaluations
to follow the same design principles even when task instances differ.
FEM 1D Tasks
The FEM 1D tasks represent the simplest end of the FEM spectrum and emphasize fundamental ideas in discretization,
element assembly, and linear elasticity. Tasks include:
• uniform mesh generation for one-dimensional domains (node coordinates and element connectivity),
• closed-form local stiffness matrices for linear 1D elastic bars,
• element-level force and displacement computation for 1D linear elasticity.
These tasks test whether models can reproduce basic FEM building blocks, manipulate simple numerical expressions,
and assemble element-wise contributions into global vectors and matrices for 1D FEM problems.

Table 1: Summary of FEM-Bench 2025 Benchmark Tasks. Tasks are grouped by domain and labeled using the
CC/H/T convention: CC = conceptual challenge level, H = number of helper functions used in the reference implementation, T = tier of helper functions provided to the LLM.
Domain

Task Name

Description

CC

H

T

local elastic stiffness
uniform mesh

Solve 1D linear elasticity
Local element stiffness matrix
Uniform 1D mesh

quad quadrature

quad8 element distributed load

quad8 integral of derivative

quad8 mesh rectangle
quad8 physical gradient

quad8 shape fcns and derivatives
tri quadrature

tri6 mesh rectangle

tri6 shape fcns and derivatives

Quadrature points and weights over reference
square
Equivalent nodal load for a distributed load applied to an edge of a Q8 element
Integral of the gradient of a scalar ﬁeld over a
Q8 element
Mesh with Q8 elements on a rectangular domain
Scalar ﬁeld gradient in physical domain on Q8
element
Shape functions and derivatives for Q8 elements
Quadrature points and weights over reference triangle
Mesh with Tri6 elements on a rectangular domain
Shape functions and derivatives for Tri6 elements

assemble global linear elastic stiffness
assemble global linear elastic stiffness
assemble global load

local elastic stiffness
local element loads
local element loads
local geometric stiffness

partition DOFs
solve eigenvalue

solve eigenvalue

solve linear
solve linear
transformation matrix

Assemble global elastic stiffness matrix
Assemble global elastic stiffness matrix
Assemble global nodal load vector
Small displacement linear-elastic analysis
Small displacement linear-elastic analysis
Local elastic stiffness matrix
Local internal nodal force/moment vector
Local internal nodal force/moment vector
Local geometric stiffness matrix with torsionbending coupling
Partition global DOFs into free and ﬁxed sets
Eigenvalue analysis given boundary conditions
and global stiffness matrix
Eigenvalue analysis given boundary conditions
and global stiffness matrix
Solve nodal displacement and support reactions
Solve nodal displacement and support reactions
3D beam transformation matrix

FEM 2D Tasks
The FEM 2D tasks introduce richer geometry, higher-order interpolation, multidimensional quadrature, and elementlevel integration. The suite includes:
• shape function evaluation and derivative computation for six-node triangular elements (Tri6) and eight-node
quadrilateral elements (Quad8),
• reference-element quadrature rules for triangles and quadrilaterals,
• geometric mappings, including gradient transformations for Quad8 elements,
• mesh generators for structured triangular and quadrilateral meshes,
• element-level integrals such as distributed loads and derivatives of shape functions.
These tasks require spatial reasoning about reference and physical coordinates, correct use of Jacobians, and handling of polynomial shape functions and Gauss–Legendre quadrature. They collectively represent the foundational
components of two-dimensional ﬁnite element formulations.
MSA 3D Tasks
The MSA 3D tasks comprise the largest and most diverse portion of the suite. They reﬂect the structure of classical
3D frame and beam formulations and require reasoning about local and global coordinate systems, element stiffness
and load routines, and global assembly. This family includes:
• local element routines such as 3D elastic stiffness matrices, geometric stiffness matrices, and internal load
vectors for Euler–Bernoulli beams,
• coordinate transformation matrices for mapping between local and global frames,
• degree-of-freedom partitioning based on boundary conditions,
• global assembly of elastic and geometric stiffness matrices and global load vectors,
• small-displacement, linear-elastic frame solves, including global displacements and support reactions,
• generalized eigenvalue problems for elastic critical-load (buckling) analysis.
These tasks exercise multiple layers of structured reasoning, including transformation of element-level matrices, proper
handling of rigid-body modes, linearity and superposition, local-to-global coupling, and the correct extraction and
partitioning of free and ﬁxed degrees of freedom. Many tasks combine geometric reasoning with matrix manipulation,
highlighting the interplay between physics-based modeling and numerical implementation.
This structure makes the MSA 3D collection especially convenient, since it provides a fully worked, self-contained
reference pathway through the classical matrix structural analysis formulation that historically served as the precursor
to modern ﬁnite element methods. By spanning element routines, transformations, assembly, and global solution procedures, these tasks offer an accessible and interpretable entry point for LLM researchers who may be unfamiliar with
mechanics yet want to study code generation in a setting grounded in well-established numerical practices. For this
reason, the MSA 3D family is the most fully developed portion of the FEM-Bench 2025 suite. Additional background
on MSA and its relationship to contemporary FEA formulations is provided in Appendix A.
Summary of Task Coverage
Taken together, the FEM 1D, FEM 2D, and MSA 3D tasks form a progression from simple element formulas to
multi-element global solvers. The suite spans interpolation, differentiation, quadrature, transformation, stiffness and
load assembly, and both linear and eigenvalue solution procedures. This diversity enables evaluation of models on
granular, element-level computations as well as multi-step synthesis problems that require chaining multiple FEM or
MSA concepts. Because each task is paired with reference implementations, veriﬁcation inputs, and pytest-based unit
tests, the suite provides a rigorous and interpretable foundation for assessing physics-based code generation.
3.8

Large Language Model Selection

We evaluate FEM-Bench using a broad selection of commercial and open-weight LLMs, chosen to represent different
model families, training strategies, and performance tiers [Liang et al., 2022]. Ten models are included in the FEMBench 2025 release, selected for their recency, API availability, and relevance to scientiﬁc computing tasks. Our

Table 2: Large Language Models Evaluated in FEM-Bench 2025. The suite includes a mix of proprietary (APIbased) and open-weights models to assess performance across different architectures and accessibility levels. Models
are categorized by their primary training focus (General vs. Coding-Specialized) and reasoning capabilities. Note that
temperature was set to 0.1 for all models. For Gemini 3 Pro Preview, thinking level was additionally set to high. For
GPT-5 and GPT-5 Mini, reasoning effort was set to high; however, temperature was not conﬁgurable for these models.
Model Name

Developer

Access

Params*

Primary Focus

Proprietary / API-Based
Gemini 3 Pro Preview Google
Google
Anthropic
Anthropic
OpenAI
OpenAI

Advanced Multimodal Reasoning
General Reasoning and Thinking
Agentic Coding and Reasoning
Fast and Efﬁcient Coding
General Reasoning and Coding
Fast Reasoning

480B
80B
400B
109B

Agentic Coding Specialist
Efﬁcient Reasoning and Coding
Multimodal Understanding
Ultra-Long Context (10M tokens)

Alibaba Cloud
Alibaba Cloud
Meta
Meta

*Parameter counts for open-weights models are approximate active parameters or total dense parameters where applicable.
Proprietary model sizes are undisclosed.

selection criteria emphasizes a comparison between proprietary models (OpenAI, Google, Anthropic) and state-ofthe-art open-weight models (Meta, Qwen), while also targeting the trade-offs between ﬂagship capabilities and the
lower inference costs of efﬁciency-focused variants. The full set of evaluated models includes Gemini 3 Pro (Preview),
Gemini 2.5 Pro, Claude Opus 4.5, Claude Haiku 4.5, GPT-5, GPT-5 Mini, Qwen3 Coder, Qwen3 Next, Llama 4
Maverick, and Llama 4 Scout. More information regarding the models can be found in Table 2,

Results and Discussion

This Section quantiﬁes how current LLMs perform on FEM-Bench 2025. Section 4.1 examines performance at the
task level, Section 4.2 compares performance across LLMs, and Section 4.3 analyzes the types of errors that appear in
LLM-generated code.
4.1

FEM-Bench 2025: Task Performance

As a ﬁrst pass assessment of LLM performance on FEM-Bench 2025, we evaluated all ten models on the full set of 33
tasks. Table 3 reports function correctness for each model and task based on a single run. To assess the stability and
variability of model outputs, Table 4 presents the results of running the three leading state-of-the-art LLMs from major
providers (OpenAI, Google, and Anthropic) ﬁve times per task and reporting how many of those attempts produced
a correct solution. Finally, Table 5 summarizes joint test success rates for all models, indicating how reliably each
models generated unit tests both validate the reference implementation and detect expected failures.
Taken together, the three tables show that no model completed the full FEM-Bench 2025 suite. For function correctness, the strongest model (Gemini 3 Pro) solved 30 of 33 tasks when counting any success across ﬁve attempts, and
26 of 33 tasks when requiring perfect consistency across all ﬁve attempts. Table 4 also highlights a subset of 11 tasks
on which all top-performing models achieved perfect (5/5) correctness: FEM 1D linear elastic T0, FEM 2D tri
quadrature T0, FEM 2D tri6 mesh rectangle T0, FEM 2D tri6 shape fcns and derivatives T0, MSA 3D
assemble global geometric stiffness T1, MSA 3D assemble global linear elastic stiffness T1, MSA
3D assemble global load T0, MSA 3D elastic critical load T1, MSA 3D linear elastic T1, MSA 3D
local element loads T3, MSA 3D solve eigenvalue T1. As Table 3 and 4 show, 19 tasks exhibiting mixed
performance and substantial variability across systems. And, a small but important group of tasks was not solved even
once by any model:MSA 3D assemble global geometric stiffness T3, MSA 3D elastic critical load T3,

MSA 3D local geometric stiffness T0. These observations conﬁrm that FEM-Bench spans a meaningful and
discriminative range of difﬁculty.
More broadly, the results show that LLMs can reliably reproduce core ﬁnite element building blocks such as basic
discretization (FEM 2D) and linear elastic analysis (FEM 1D and many MSA 3D tasks), but struggle as tasks introduce geometric nonlinearity or require reasoning beyond direct formula application. Performance within the MSA 3D
domain illustrates this progression most clearly: models succeed on the simplest routines yet consistently fail when required to perform geometric nonlinear analysis without helper functions. These unsolved tasks and their characteristic
failure modes are examined in more detail in Section 4.3.
Test generation results in Table 5 mirror the trends observed in function correctness. Simple tasks exhibit uniformly
high joint success across models, intermediate tasks show substantial variability, and the most complex tasks, particularly those involving geometric stiffness or buckling in MSA 3D, yield joint success rates that are effectively zero for
all models. For FEM 1D and most FEM 2D tasks, the strongest models achieve joint success near 100%, indicating
that they can generate tests that both validate correct implementations and detect known failure modes. Performance
deteriorates on more demanding FEM 2D tasks and collapses entirely on nonlinear MSA tasks, even when some
models produce correct code. These results suggest that writing discriminative, physics-aware tests is at least as challenging as writing the underlying routines. Overall, the joint test outcomes reinforce that FEM-Bench 2025 provides
a meaningful and sensitive assessment of the current limits of LLMs in scientiﬁc computing.
4.2

FEM-Bench 2025: LLM Ranking

Figure 3 summarizes model performance by plotting function correctness (x-axis) against average joint test success
(y-axis), revealing a clear separation between model families and capability tiers. The ﬂagship closed-weight models
cluster in the upper-right region of the plot, showing substantially higher performance compared to the other models,
which occupy the lower-left region. For successful task completion (i.e., function correctness) Gemini 3 Pro (Preview)
(29/33 tasks correct) and Claude Opus 4.5 (28/33 tasks correct) are the best performing models. For Joint Test Success
Rate, GPT-5 (73.8 %) is the best performing model while Claude Opus 4.5 (71.9 %) and Gemini 3 Pro (Preview) (71.6
%) perform comparably. Notably, development of FEM-Bench began in summer 2025, and several of the models
evaluated here already demonstrate signiﬁcantly stronger performance than models available at that time, underscoring
the rapid pace of progress. As model capabilities continue to grow, future versions of FEM-Bench must incorporate
more challenging and diverse tasks to ensure that the benchmark remains discriminative and reﬂective of the evolving
state of the ﬁeld.
4.3

FEM-Bench 2025 Error Analysis

Although FEM-Bench 2025 contains only 33 tasks, its structure enables clear and interpretable error analysis. The
benchmarks modularity, controlled variations in helper-function availability, and pairing of related tasks at increasing
levels of complexity allow us to isolate where and why LLMs fail in computational mechanics workﬂows. Based on
the unsolved tasks and informed by current understanding of LLM failure modes [Jiang et al., 2024, Shi et al., 2023,
Pinto et al., 2024, Gottweis et al., 2025], we group errors into three broad categories: (1) domain knowledge deﬁcits,
(2) compositional reasoning deﬁcits, and (3) algorithmic ﬁdelity deﬁcits:
• Domain Knowledge Deﬁcit: The model lacks accurate or sufﬁciently detailed knowledge of the
underlying mechanics, formulas, or numerical structures required for the task. For example, on
MSA_3D_local_geometric_stiffness_CC1_H0_T0 which requires only generating the local geometric stiffness matrix with no compositional steps, gemini-3-pro-preview produce syntactically valid code, yet it is
missing axial-rotation coupling terms and uses incorrect moment-displacement coupling formulas.
• Compositional Reasoning Deﬁcit: The model has access to the relevant components either via provided
helper functions or its training data, but fails to combine and manipulate these components correctly in multistep computations. For instance, LLaMA-4-scout correctly implements the shape function derivative on
FEM_2D_quad8_physical_gradient_CC0_H1_T3 but fails to call it correctly in the subsequent computational
step.
• Algorithmic Fidelity Deﬁcit: The model understands the intended computation but cannot maintain the
precision and consistency required to implement it faithfully, leading to indexing errors, incomplete routines, inconsistent conventions, or structurally invalid outputs. In FEM-Bench 2025, this failure mode arises
predominantly in lower-performing models and often manifests as code that loses logical structure, mixes
incompatible conventions, or fails to execute. This behavior is closely related to what is commonly described as instruction-following failure in general LLM benchmarks [Ouyang et al., 2022], but here appears
in a domain-speciﬁc form tied to the execution of numerical algorithms. For example claude-haiku-4.5

Table 3: Function Correctness on FEM-Bench Tasks. 3 indicates successful task completion.

29/33

26/33

28/33

19/33

22/33

25/33

21/33

6/33

Total Passed

Table 4: Function Correctness out of 5 runs on FEM-Bench Tasks for the top performing LLMs.

Tasks Solved (any success)
Tasks Solved (5/5 success)

30/33
26/33

29/33

28/33
19/33

Table 5: Joint Test Success Rate (%) on FEM-Bench Tasks. A “—” symbol indicates that the model did not produce
parsable code, and is treated as 0% when aggregating scores.

80.0

20.0

80.0

Avg. Joint Success

71.6

63.4

71.9

49.5

73.8

65.4

41.8

49.3

41.4

37.2

Figure 3: Comparison of model performance on FEM-Bench 2025. The plot shows function correctness versus average
joint test success rate for all evaluated models (pulled from Table 3 and Table 5 data), illustrating clear capability
differences across model families and identifying the current performance frontier.
on FEM_2D_quad8_physical_gradient_CC0_H1_T3 reassigns dN_dxi[0] over 80 times in a loop, cycling
through different formulas as if reasoning out loud and ultimately fails to produce a complete implementation.
FEM-Bench is well suited to distinguishing these deﬁcits because its tasks share common computational patterns while
varying in domain knowledge load and reasoning depth.
Figure 4 highlights the difference in difﬁculty between two key tasks in FEM-Bench. In the reference implementation
for linear-elastic problems (Fig. 4i), the workﬂow ends once the global stiffness matrix and load vector are assembled
and a single linear solve is performed. In Appendix A, we provide a more detailed explanation of the building blocks of
this schematic for readers who are new to the ﬁeld. With this level of difﬁculty, the strongest models reliably succeed.
In contrast, a representative more difﬁcult tasks, MSA 3D elastic critical load analysis (Fig. 4ii) includes additional
stages: extracting the displacement ﬁeld from a prior analysis, assembling the geometric stiffness matrix, coupling
it with the elastic stiffness matrix, and solving a generalized eigenvalue problem. This expanded pipeline introduces
both an increased requirement for domain knowledge, and increased demands on compositional reasoning.

(i) Schematic of linear elastic analysis reference implementation
INPUT

Linear solve

OUTPUT

(ii) Schematic of elastic critical load analysis reference implementation
INPUT
Linear solve

Eigenvalue analysis

OUTPUT

Local element loads

Figure 4: Schematic comparison of the reference implementations used in FEM-Bench for (i) linear elastic analysis
(a solved task) and (ii) elastic critical load analysis (a currently unsolved task). In both cases, the workﬂow begins by
assembling the global load vector F and global elastic stiffness matrix K from local element contributions, followed
by partitioning degrees of freedom and performing a linear solve. For elastic critical load analysis, the converged
displacement ﬁeld is used to assemble the geometric stiffness matrix Kgeom , after which an eigenvalue analysis is
performed to compute critical loads. The outputs consist of nodal displacements and reactions for the linear case, and
critical load factors and mode shapes for the buckling case. Note that the elastic critical load analysis contains the
linear elastic analysis within it.
The challenge level of the MSA 3D elastic critical load analysis task is further illustrated by the Tier 1, Tier 2, and Tier
3 variants. When helper functions are fully provided and the task reduces to chaining them together (T1), most LLMs
are able to succeed. When the geometric stiffness matrix is provided but no other helpers are available (T2), ﬂagship
models succeed the majority of the time (Table 4), although several other models still fail (Table 3). However, when
no helpers are provided (T3), all models fail. This outcome is consistent with the observation that no model is able to
generate the local geometric stiffness matrix in the related task MSA_3D_local_geometric_stiffness_matrix_T0.
From an error analysis perspective, these results show that all models exhibit a domain knowledge deﬁcit with respect
to geometric stiffness, and that poorer performing models additionally exhibit compositional reasoning deﬁcits when
required to integrate partially provided components. This aligns with the broader mechanics literature, where geomet26

ric stiffness formulas are less standardized, appear inconsistently in reference materials, and require understanding of
geometrically nonlinear behavior that is both less common and more challenging than linear elastic analysis to parse
correctly. A major avenue of future work for FEM-Bench development is creating more tasks for side-by-side comparison across different compositional reasoning and domain knowledge requirements with challenge modulated via the
number of helper functions provided (tiers).
A notable discrepancy also appears between code correctness and test correctness. Even when top models produce
correct implementations for tasks, they may not be able to generate effective unit tests. Writing tests in FEM-Bench
requires identifying and articulating concepts such as symmetry, rigid-body modes, and analytical displacement relationships, as well as constructing small subproblems that expose speciﬁc failure modes. These activities often require
more explicit reasoning and domain insight than straightforward code writing. A clear example of this can be seen in
Listing 2 where the main code involves returning a 12×12 stiffness matrix while the two required test codes involve
(1) checking the properties of the matrix, and (2) checking if the matrix can be used to match analytical equations.
From Table 3 and Table 5, we see that LLM performance on function writing exceeds performance on unit test writing
for this task. Overall, joint test success deteriorates rapidly as task complexity increases, even in cases where function
correctness remains high. It is also possible that unit test underperformance reﬂects the relative scarcity of physicsbased test code in typical LLM training corpora. Understanding the extent to which training data, task structure, and
model reasoning contribute to this gap is an interesting direction for future study.
It is also worth noting that LLM performance is often highly sensitive to prompt choice [Liu et al., 2023]. Although a
comprehensive ablation study or systematic comparison of prompt formulations is beyond the scope of this work, we
conducted a targeted exploration using the GEPA prompt optimization technique, described in Appendix D. Our goals
were twofold: (1) to verify that model performance was not being limited by simple but impactful prompt reﬁnements,
and (2) to assess whether adding speciﬁc information through a system prompt could meaningfully improve performance and thereby illuminate the error mechanisms discussed in Section 4.3. As detailed in Appendix D, GEPA did
not yield any generic improvements, such as impactful instructions to think carefully or focus on correctness. However,
GEPA was able to produce meaningful gains when it incorporated domain knowledge extracted from the training tasks
into the system prompt. These ﬁndings reinforce that our prompts are already strong and also support the conclusion
that domain knowledge deﬁcits, rather than lack of generic reasoning guidance, are a primary source of the errors
observed in FEM-Bench 2025.
Taken together, these observations illustrate the current state of LLMs in computational mechanics. Models can reproduce foundational FEM building blocks when the domain knowledge burden is low, and they can often execute
multi-step workﬂows when critical domain components are provided. However, they struggle in some cases where
domain knowledge must be inferred, composed, or reconstructed, and they struggle even more when asked to express
correctness criteria through physics-aware unit tests. These ﬁndings, along with the trend towards improved performance shown in Fig. 3, emphasize the need for future versions of FEM-Bench to include tasks that continue to probe
the boundaries between domain knowledge, multi-step reasoning, and algorithmic precision.

Conclusion

FEM-Bench 2025 provides a ﬁrst systematic assessment of LLM capabilities in computational mechanics, revealing
that while current models can reliably reproduce many foundational FEM and MSA routines, they still struggle with
more complex tasks in the domain. The benchmark highlights both the substantial progress made by state-of-the-art
systems and the persistent gaps that arise in geometric nonlinear analysis, eigenvalue buckling problems, and tasks
requiring discriminative unit tests. These results underscore that LLMs are not yet ready to autonomously implement
or verify advanced scientiﬁc computing workﬂows, but they are increasingly capable of contributing meaningfully
to structured numerical tasks. Reported successes of state-of-the-art LLMs in generating advanced FE code or
manuscript-style derivations typically involve agentic workﬂows with iterative execution feedback Deotale et al.
[2026], Hang et al. [2026], which can compensate for domain-knowledge gaps through trial and error. This iteration
of FEM-Bench probes the complementary and more fundamental capability of single-pass reasoning without such
scaffolding. Future iterations of FEM-Bench will expand in this direction
FEM-Bench is designed as a living benchmark: the evaluation pipeline is fully automated and can be re-run as new
models are released, enabling continual tracking of progress. Its modular, source-ﬁrst structure also makes the benchmark highly extensible, allowing new tasks to be added as existing ones are mastered. At present, we are working on a
next suite of tasks that are more challenging than the ones presented in this initial work. Speciﬁcally, our future work
will substantially expand the task suite to cover a broader range of mechanics problems, including nonlinear material
behavior, dynamic analysis, incompressible elasticity and associated numerical challenges, and multiphysics coupling.

Simultaneously, we are interested in using FEM-Bench as a foundation for studying more sophisticated LLM-assisted
and agentic workﬂows for scientiﬁc computing within the broader ecosystem of AI-driven scientiﬁc analysis and discovery [Cai et al., 2025, Shojaee et al., 2025, Song et al., 2025]. Beyond expanding the task suite, future work
could also explore ﬁne-tuning open-weight models on FEM-Bench tasks to assess whether domain-speciﬁc training
closes the performance gap on the most challenging problems in the suite. In future versions of FEM-Bench, we will
also extend the evaluation methodology by incorporating partial-credit metrics, to provide a better characterization of
model weaknesses. For example, recent work has explored using a separate LLM, ﬁne-tuned as a judge, to evaluate
the reasoning and assign partial credit [Xia et al., 2025, Hao et al., 2024, Tong and Zhang, 2024] as well as automated
evaluation approaches that measure the consistency of the reasoning steps against a reference solution graph Yang
et al. [2025]

Acknowledgments

The authors gratefully acknowledge support from the Boston University Department of Mechanical Engineering, the
National Science Foundation through the CSSI Elements program (Grant No. CMMI-2310771), the Amazon Research
Award program, and the BU SAIL AI Pipeline Pilot.

Additional Information

The FEM-Bench software and all code to reproduce this work is available on GitHub https://github.com/
elejeune11/FEM-bench.

A Primer on Matrix Structural Analysis for Large Language Model Researchers
A natural point of departure for understanding matrix structural analysis (MSA) and the ﬁnite element method (FEM)
is the material covered in an introductory physics class, where the relationship between force and displacement is
introduced through Hooke’s law:
f = k δ.
This scalar equation expresses the idea that an elastic spring resists deformation in direct proportion to its stiffness.
MSA and FEM generalize this relationship to systems composed of many interconnected components. A structure
is discretized into elements (such as springs, truss bars, beam segments, or volumetric components) connected at
nodes, and each node can translate or rotate in space depending on the degrees of freedom allowed by the modeling
assumptions (see also Fig. 1).
In this discretized setting, the simple spring law becomes a vector–matrix relation of the form
F = K ∆,

(2)

where
• F is the global vector of nodal forces and moments,
• K is the assembled global stiffness matrix, formed by superposing contributions from all elements, and
• ∆ is the global vector of nodal displacements and rotations.
Equation (2) is therefore a direct multidimensional analogue of Hooke’s law. Instead of a single stiffness constant k,
the stiffness matrix K encodes how each degree of freedom in the structure resists deformation and how deformations
at one node inﬂuence forces at another. Likewise, the displacement vector ∆ extends the scalar displacement x to
include translations and rotations at all nodes in the discretized model. This process is illustrated schematically in Fig.
5. Although more advanced MSA and FEM formulations often look much more complex, this linear algebraic form
provides a straightforward fundamental starting point. From a programming perspective, even this simple relation
requires careful construction of element contributions, consistent indexing of degrees of freedom, robust assembly
procedures, and reliable linear algebra operations, all of which present meaningful challenges for LLMs tasked with
generating correct scientiﬁc code.
A.1

Historical Context, relationship between Matrix Structrual Analysis and Finite Element Methods

Matrix Structural Analysis (MSA) is the foundational framework from which Finite Element Analysis (FEA) evolved.
MSA focuses on representing structures (e.g., trusses, beams, and frames) using stiffness matrices and equilibrium

Input
nodes

Solve

elements

Define

(section properties,
material properties,
nodal connectivity)
boundary
conditions

•

(displacement)

•

(reaction force:
at fixed
boundaries)

nodal loads

Input
• nodal coordinates

Define
assemble

• element information
• boundary conditions
• nodal loads

assemble

Solve
linear system
of equations

local element stiffness
transform local to global

Figure 5: Illustration of the Matrix Structural Analysis workﬂow. A structural frame is discretized into nodes and
elements with associated material and section properties, boundary conditions, and nodal loads. These inputs are used
to assemble the global load vector and global stiffness matrix by computing local element stiffnesses and transforming
them to global coordinates. The resulting system F = K∆ is then solved for nodal displacements and support
reactions.
equations, providing an efﬁcient way to analyze linear structural systems. FEA generalizes these same principles to
continuous domains and complex geometries, extending the matrix-based formulation of MSA to handle arbitrary
shapes, materials, and boundary conditions in a wide range of physical problems. Both share a common mathematical
structure: assembling element stiffness matrices into a global system of equations that relates nodal forces to displacements. Today, MSA can be viewed as a special case of FEA, applicable to structures composed of beam- or frame-like
elements. Both methods follow a similar computational structure and high level workﬂow.2
A.2

Deriving Linear Equations via the Direct Stiffness Method

There are several ways to derive Eq. 2 for matrix structural analysis problems. The most accessible is the Direct
Stiffness Method (DSM), which constructs global equilibrium equations directly from element-level stiffness relations. Although modern ﬁnite element formulations typically rely on the Principle of Virtual Work (PVW) or the
weak form of the governing equations (these approaches generalize naturally to two- and three-dimensional continua)
the algebraic structure that emerges is the same. For instructional purposes, the Direct Stiffness Method provides a
transparent entry point: it exposes each computational component (element stiffness, coordinate transformation, assembly, and application of boundary conditions) explicitly, without requiring the variational machinery behind full
FEM. Using the Direct Stiffness Method, Eq. 2 can be formulated through the following basic procedure:
1. Discretize the structure into nodes and elements, deﬁning connectivity.
2. Establish local element stiffness matrices.
3. Transform local matrices to the global coordinate system.
4. Assemble the global stiffness matrix from the transformed local element stiffness matrices.

https://quickfem.com/wp-content/uploads/IFEM.AppH_.pdf

5. Partition the global system to apply boundary conditions.
6. Solve for unknown displacements.
7. Post-process to compute forces, moments, and deﬂections.
8. Extend for further analysis (e.g., buckling, nonlinear behavior).
Step 1: Discretization
In 3D, we discretize the structure into a ﬁnite number of nodes and elements that capture its geometry and connectivity. Each node represents a point where displacements and rotations are deﬁned, serving as the connection between
adjacent elements (see Fig. 5).
• Each node possesses six degrees of freedom (DOFs): translational (u, v, w) and rotational (θx , θy , θz ) components.
• Each beam element connects two nodes, leading to a total of 12 DOFs per element.
This discretization transforms a continuous structure into a discrete model suitable for matrix-based analysis, where
the deformation of the entire structure is represented by the collective motion of its nodes.
Step 2: Establish Local Element Stiffness Matrices
Each beam element is ﬁrst described in its own local coordinate system, whose axes are aligned with the elements
geometry (typically with the local x-axis along the element length and the local y- and z-axes deﬁning transverse
directions). In this coordinate system, the element stiffness relation takes the form
Flocal = klocal ∆local ,

(3)

where Flocal is the 12 × 1 vector of nodal forces and moments, ∆local is the 12 × 1 vector of nodal displacements and
rotations, and klocal is the 12 × 12 local element stiffness matrix, all in local coordinates.
For a 3D frame element, klocal combines contributions from axial deformation, torsion, and bending about both
the local y- and z-axes. Each contribution can be written in the form F = k ∆ with explicitly labeled force and
displacement components deﬁned in the local coordinate system:
• Axial (along local x):

][ ]
Fx1
EA 1 −1 ux1
,
L −1 1
Fx2
ux2
where ux1 and ux2 are axial displacements at nodes 1 and 2, and Fx1 and Fx2 are the corresponding axial
forces.
• Torsion (about local x):
][ ]
Mx1
GJ 1 −1 θx1
,
L −1 1
Mx2
θx2
where θx1 and θx2 are rotations about the local x-axis at nodes 1 and 2, and Mx1 and Mx2 are the corresponding torsional moments.
• Bending about z (deﬂection v and rotation θz ):
 

6L −12 6L
v1
Fv1
M  EI  6L 4L2 −6L 2L2  θ 
  z1 
 z1 
z 
 ,
= 3 

L −12 −6L 12 −6L  v2 
 Fv2 
Mz2

2L2

−6L

4L2

θz2

where v1 and v2 are transverse displacements in the local y-direction and Mz1 and Mz2 are bending moments
about the z-axis at nodes 1 and 2.
• Bending about y (deﬂection w and rotation θy ):

 
12 −6L −12 −6L
w1
Fw1

M  EI −6L 4L2
2
θ
2L
 y1 
  y1 
y 
= 3 

 ,
L  −12 6L
 Fw2 
6L   w2 
My2

−6L

2L2

4L2

θy2

where w1 and w2 are transverse displacements in the local z-direction and My1 and My2 are bending moments
about the y-axis at nodes 1 and 2.
Derivations for each of these submatrices follow from classical Euler–Bernoulli beam theory, where axial, torsional,
and bending deformations are expressed in terms of the elements material and geometric properties. By assembling
these submatrices along the diagonal, we obtain the full 12 × 12 local stiffness matrix k that captures both material
properties (E, G) and geometric properties (A, Iy , Iz , J, L). This local matrix serves as the foundation for the coordinate transformation to the global system in Step 3, and ultimately for assembling the contributions of many elements
into a single global system of equilibrium equations.
Step 3: Transform Local Matrices to the Global Coordinate System
Each element stiffness matrix is ﬁrst deﬁned in its local coordinate system (Flocal , ∆local ), where the x′ -axis aligns
with the elements longitudinal axis. To express the element behavior in the global coordinate system (F, ∆), we apply
a coordinate transformation using the orthogonal transformation matrix Γ, constructed from the elements direction
cosines. The transformation relates local and global displacement and force vectors as:
∆local = Γ∆,

Flocal = ΓF.

(4)

Substituting into the local stiffness relation Flocal = klocal ∆local gives the global form:
F = ΓT klocal Γ∆,

(5)

k = ΓT klocal Γ.

(6)

so that the global element stiffness matrix is:

The matrix Γ depends on the element orientation, with direction cosines derived from the elements local and global
axes. For 3D frames, Γ is block-diagonal, containing four identical 3 × 3 rotation submatrices based on these cosines.
Step 4: Assemble Global Stiffness Matrix
After transforming each element stiffness matrix to the global coordinate system, all element contributions are assembled into the global stiffness matrix K. Assembly is performed by mapping each element’s local degrees of freedom
(DOFs) to the corresponding entries in the global stiffness matrix using the element’s DOF index list. For each element
elem, the global DOF indices are stored in a dof_map array (e.g., a list of length 12 for a 3D beam), and the local
stiffness matrix k_elem is accumulated into the global matrix K using standard row–column indexing:
K[dof_map, dof_map] += k_elem.

(7)

This operation superposes the element’s contribution onto the appropriate global DOF locations, consistent with the
direct stiffness method and modern ﬁnite element assembly procedures.
This process is repeated for all elements, resulting in the global equilibrium relation:
F = K∆.

(8)

The assembled K is symmetric and sparse, with nonzero entries only at DOF pairs that belong to the same or adjacent
connected elements.
Step 5: Partition the Global System to Apply Boundary Conditions
To incorporate boundary conditions, the global equilibrium system is partitioned into free and constrained degrees of
freedom (DOFs):
][ ] [ ]
Ff
Kﬀ Kfc ∆f
(9)
.
Kcf Kcc ∆c
Fc
Prescribed displacements (e.g., ﬁxed or pinned supports) are enforced by setting ∆c to known values (often 0), and
the reduced system
Kﬀ ∆f = Ff − Kfc ∆c

(10)

is solved for the unknown free displacements. This partitioning cleanly separates supported and unconstrained DOFs
for efﬁcient solution and reaction recovery.
Step 6: Solve for Unknown Displacements

With boundary conditions applied, the reduced equilibrium system
Kﬀ ∆f = Ff − Kfc ∆c

(11)

is solved for the unknown nodal displacements ∆f using numerical linear algebra techniques (e.g., Gaussian elimination or sparse matrix solvers). Once ∆f is obtained, the reactions at constrained DOFs are recovered from:
Fc = Kcf ∆f + Kcc ∆c .

(12)

This step yields the complete displacement ﬁeld and reaction forces for the structure.
Step 7: Post-process to Compute Forces, Moments, and Deﬂections
After obtaining nodal displacements, internal element forces and moments are recovered using the local stiffness
relation:
local
local
Flocal
element = kelement ∆element ,

(13)

where ∆local
element = Γ∆element are the element deformations expressed in the local coordinate system. From these
quantities, one can compute axial forces, shear forces, bending moments, and torsion along each element, as well as
visualize the deﬂected shape of the structure. These results are typically presented graphically to assess structural
performance and verify design requirements.
A.3

Elastic Critical Load Analysis

Elastic critical load analysis determines the maximum load a structure can sustain before experiencing elastic buckling,
assuming the material remains within its elastic limit. Buckling is characterized by a sudden lateral deformation under
compressive loading and is governed by the eigenvalue problem:
[Kelastic + λKgeometric ] ∆ = 0,

(14)

where Kelastic is the elastic stiffness matrix, Kgeometric is the geometric stiffness matrix computed with respect to a
reference load Pref , λ is the load factor (eigenvalue), and ∆ is the buckling mode shape (eigenvector). The smallest
eigenvalue λcr corresponds to the elastic critical load, Pcr = λcr Pref , and its associated eigenvector deﬁnes the buckled
conﬁguration.
The geometric stiffness matrix Kgeometric captures the inﬂuence of axial forces on lateral displacements through both
global (P –∆) and local (P –δ) effects. Its derivation involves applying the principle of virtual work with nonlinear
strain terms and incorporating axial, ﬂexural, and torsional contributions. A full derivation of Kgeometric can be
found in standard Matrix Structural Analysis (MSA) textbooks, where expressions for the axial, ﬂexural, and torsional
geometric stiffness components are developed in closed form [McGuire et al., 2000].
A.4

Numerical Challenges

In Matrix Structural Analysis (MSA), numerical challenges become especially evident when solving the generalized
eigenvalue problem for elastic critical load analysis. Small numerical errors can strongly inﬂuence the computed
eigenvalues and corresponding buckling modes. Finite precision arithmetic introduces rounding and truncation errors
that accumulate during matrix assembly and factorization, while ill-conditioned stiffness matrices amplify these errors.
The condition number κ(K) serves as a key indicator of numerical sensitivity: as κ increases, signiﬁcant digits are
lost in both displacement and eigenvalue computations. Discretization adds further complexity–although reﬁning the
mesh or using higher-order shape functions improves the approximation of the true (sinusoidal) buckling shape, it
also increases κ(K), making the eigenvalue problem more sensitive to ﬂoating-point precision. As a result, accurate
computation of critical loads requires balancing discretization quality and numerical stability, often necessitating the
use of robust linear algebra routines for large or ill-conditioned systems. Though the benchmark does not touch on
this area extensively, it is a rich direction for further development in that understanding these errors often requires
sophisticated reasoning and expertise across multiple domains.
A.5

Additional Pedagogical Resources

For readers interested in more general derivations of Matrix Structural Analysis, the Principle of Virtual Work (PVW)
provides a powerful and elegant framework from which the element stiffness relations and global equilibrium equations
can be derived. PVW also offers a direct bridge to ﬁnite element formulations, where the same variational principles
are applied to continuous domains to obtain weak forms, interpolation functions, and numerical integration rules.

Similar PVW-based derivations for the ﬁnite element method can be found in standard FEM texts, where beam, truss,
solid, and shell elements are introduced as speciﬁc discretizations of the governing partial differential equations. These
derivations highlight the shared mathematical structure between MSA and FEM while also illustrating how FEM
extends to more complex geometries and physics.
Key references on Matrix Structural Analysis include classical works such as McGuire, Gallagher, and Ziemians
Matrix Structural Analysis, which provides a clear introduction to beam and frame formulations [McGuire et al., 2000].
For ﬁnite element methods, foundational texts include (but are certainly not limited to, see for example additional
references in Sections 1 and 2) Zienkiewicz and Taylors The Finite Element Method [Zienkiewicz and Taylor, 2005],
Bathes Finite Element Procedures [Bathe, 1996], and Hughes The Finite Element Method [Hughes, 2003]. These
resources offer both theoretical background and practical insights that complement the material presented in FEMBench.

B

Inference parameters and settings for the evaluated models

This appendix summarizes the inference parameters used for each of the ten large language models evaluated in FEMBench 2025. Table 6 reports the default and maximum output token budgets, the sampling temperature, and the
reasoning effort setting for each model. The default token budget was chosen to be sufﬁciently large for all tasks in
the FEM-Bench 2025 suite, while the cap denotes the upper limit enforced by the FEM-Bench inference pipeline.
Table 6: Inference settings for the models evaluated in FEM-Bench 2025. The default token budget is used unless
overridden, the cap denotes the upper limit enforced by the FEM-Bench inference pipeline. Temperature was set to 0.1
and reasoning effort to “high” where supported. A dash indicates that the parameter is not conﬁgurable for the model.
Model

Default

Cap

Temperature

Reasoning Effort

Gemini 3 Pro Preview
Qwen3 Next 80B

32,000
24,000
6,000
15,000
15,000
16,000
16,000
8,000
8,000

65,536
65,000
32,000
8,192
32,768
32,768
16,384
16,384

C Tests and expected failure cases
In this appendix, we provide test and expected-failure examples from three representative FEM-Bench tasks. Table 7
lists the category of each unit test along with a description of what it veriﬁes, and Table 8 summarizes each expectedfailure implementation, including its returned output and the test functions it is designed to be rejected by.

D Preliminary work on prompt optimization via GEPA
While LLMs achieve strong performance across a wide range of applications due to their broad, general-purpose
pretraining [Brown et al., 2020], attaining high performance in a speciﬁc domain often beneﬁts from an additional
post-training optimization step [Brown et al., 2020]. Post-training optimization is typically accomplished either by
ﬁne-tuning model weights or by improving the input prompts. Fine-tuning methods such as Group Relative Policy
Optimization (GRPO) [Shao et al., 2024], which was originally introduced in DeepSeekMath to enhance mathematical
reasoning in LLMs, can be effective but often require a large number of model rollouts [Agrawal et al., 2025]. Alternatively, using higher-quality prompts, including those augmented with few-shot examples, has proven highly effective
for downstream applications [Brown et al., 2020, Zhou et al., 2022]. This process of crafting prompts that elicit the

Table 7: Detailed summary of unit tests for three representative FEM-Bench tasks. Tests span three categories: physics
(veriﬁcation against analytical/closed-form solutions), numerics (mesh convergence, accuracy), and algorithm (invariance, linearity, equilibrium). All tests are available open-access on the FEM-Bench GitHub repository.
Test

Category

Veriﬁcation

Task: MSA_3D_elastic_critical_load_CC1_H10_T3
Euler buckling parameter
sweep

Physics

Orientation invariance

Mesh convergence

Cantilever circular column compared against the analytical Euler buckling load Pcr = π 2 EI/(4L2 ) across radii r ∈ {0.5, 0.75, 1.0} and
lengths L ∈ {10, 20, 40}; relative error required < 10−5 .
Rectangular-section cantilever solved before and after a rigid-body rotation R applied to geometry, element axes, and loads; veriﬁes that the
critical load factor λ is invariant and that the buckling mode transforms
as T ϕ where T is the block-diagonal rotation operator.
Reﬁnes mesh from 10 to 40 elements for a ﬁxed circular cantilever;
checks monotone decrease of the relative error against the Euler solution and requires the ﬁnest mesh to achieve error < 10−6 .

Task: MSA_3D_linear_elastic_CC0_H6_T3
Cantilever along [1, 1, 1]

Physics

Complex geometry and
loading

Physics + Algorithm

Cantilever beam discretized along the [1, 1, 1] direction with a transverse tip load; tip deﬂection compared against the Euler–Bernoulli
closed-form solution δ = P L3 /(3EI) within 2% tolerance.
Tetrahedral frame tested for: (i) zero response under zero loads, (ii)
linearity (2× load ⇒ 2× response), (iii) sign reversal under negated
loads, and (iv) global static equilibrium of reactions (force and moment
balance).

Task: FEM_2D_quad_quadrature_CC0_H0_T0
Invalid input handling

Basic structural properties

Degree exactness, 1 × 1

Degree exactness, 2 × 2

Degree exactness, 3 × 3

Veriﬁes that the quadrature routine raises a ValueError when invoked
with an unsupported number of integration points (e.g. 0, 2, 3, 5, 7), enforcing the documented contract that only {1, 4, 9} are valid.
Checks that, for each supported rule, the returned point and weight
arrays have correct shapes and dtypes, that the weights sum to 4 (the
area of the reference square [−1, 1]2 ), and that all quadrature points lie
within the reference domain.
Veriﬁes that the single-point rule integrates random polynomials with
per-variable degree ≤ 1 exactly (to within 10−13 ), and that adding
quadratic terms breaks exactness, conﬁrming the rule’s theoretical
degree-of-precision.
Veriﬁes that the 2 × 2 tensor-product rule integrates random polynomials with per-variable degree ≤ 3 exactly, and that adding quartic terms
breaks exactness.
Veriﬁes that the 3 × 3 tensor-product rule integrates random polynomials with per-variable degree ≤ 5 exactly, and that adding degree-6
terms breaks exactness.

Table 8: Expected-failure implementations for three representative FEM-Bench tasks. These are intentionally incorrect
dummy implementations that the generated tests must reject in order to demonstrate discriminative power. A test
receives credit only if it passes on the reference implementation and fails on every expected-failure implementation
listed below.
Implementation

Returned Output

Why It Should Be Rejected

Task: MSA_3D_elastic_critical_load_CC1_H10_T3
All-zeros buckling

λ = 0, mode ϕ = 0

All-ones buckling

λ = 1, mode ϕ = 1

Violates the requirement that the critical load factor be strictly
positive and that the buckling mode be a nontrivial eigenvector.
Caught by analytical comparisons against the Euler load and
by mesh convergence tests, both of which require λ > 0 and
ﬁnite, mesh-dependent values.
Returns a constant buckling factor independent of geometry/material and a mode that ignores boundary conditions (ﬁxed
DOFs are non-zero). Caught by parameter sweeps over L and
r (which require λ ∝ 1/L2 ) and by the orientation-invariance
test (which requires the mode to transform correctly under
rigid rotation).

Task: MSA_3D_linear_elastic_CC0_H6_T3
All-zeros linear elastic

u = 0, r = 0

All-ones linear elastic

u = 1, r = 1

Returns identically zero displacements and reactions regardless of the applied load. Caught by the cantilever tip-deﬂection
test (which expects a nonzero analytical deﬂection) and by the
static equilibrium check (which requires reactions to balance
the applied loads).
Returns constant unit displacements and reactions regardless
of input. Caught by the linearity check (doubling the load
should double the response, not leave it constant), the signreversal check (negating the load should ﬂip the sign), and the
ﬁxed-DOF check (constrained DOFs must remain zero).

Task: FEM_2D_quad_quadrature_CC0_H0_T0
No-error dummy

Mis-normalized weights

Empty arrays returned
for invalid input instead
of raising
Weights normalized to
sum to 1 instead of 4

All-zeros quadrature

Points and weights
identically zero

All-ones quadrature

Points and weights
identically one

Violates the API contract by silently returning empty point
and weight arrays for unsupported num_pts rather than raising ValueError. Caught by the invalid-input test.
Returns weights whose total is the unit square area rather than
the reference square area [−1, 1]2 = 4. Caught by the basics test (weight-sum check) and by all degree-exactness tests,
which would systematically underestimate every integral by a
factor of 4.
Returns zero points and weights regardless of num_pts; any
integral of a nonzero function evaluates to 0. Caught by the
basics test (weight sum ̸= 4) and by all degree-exactness tests.
Returns unit-valued points and weights regardless of num_pts,
breaking both the point-location and weight-sum properties.
Caught by the basics test and by all degree-exactness tests.

desired model behavior is known as prompt engineering [Zhou et al., 2022]. To automate this process, a variety of
prompt optimization methods have been developed. For example, MIPROv2 [Opsahl-Ong et al., 2024] uses Bayesian
optimization to align instructions with examples in the prompt. Other approaches, such as EvoPrompt [Guo et al.,
2023] and GEPA [Agrawal et al., 2025], rely on evolutionary algorithms that treat natural language phrases as gene
sequences in order to evolve improved prompts.
In our exploration of prompt optimization, we focus on the GEPA algorithm. GEPA (Genetic-Pareto) is a prompt optimizer that combines evolutionary search with natural-language feedback generated by a reﬂective LLM to iteratively
reﬁne candidate prompts [Agrawal et al., 2025]. Within the context of FEM-Bench, GEPA performs multi-objective
optimization across tasks using a Pareto frontier, making it well suited for adapting LLMs in a sample-efﬁcient manner
on small datasets. Here, we investigate whether a GEPA-optimized system prompt can improve LLM performance on
the FEM-Bench 2025 task suite. Our objectives are twofold: (1) to ensure we are not inadvertently limiting model
performance by overlooking simple but impactful prompt improvements (for example, “think carefully” or “focus on
correctness”), and (2) to examine what additional information, when provided through the system prompt, meaningfully improves performance and whether this sheds light on the error mechanisms discussed in Section 4.3.
Because FEM-Bench 2025 only consists of 33 tasks and GEPA requires access to sample tasks for training, we restrict
our exploration to one speciﬁc and limited scenario. Speciﬁcally, we trained the GEPA optimizer on all tasks, except
Tier 1, Tier 2, and Tier 3 variants of the MSA_3D_elastic_critical_load task which is the most complex task in
FEM-bench 2025 suite encompassing all other tasks in MSA_3D domain. As presented in Table 3, the versions of
this task without helper functions provided (T3 for no helper functions, T2 for only local geometric stiffness matrix
provided) are two of the most challenging tasks for the tested models.
Our protocol is as follows. We used the GEPA optimizer implemented in the DSpy [Khattab et al., 2024, 2022]
framework, with the system-aware merge strategy which merges the prompts in the pool that have a complementary
strategy [Agrawal et al., 2025], a minibatch size of 3 and all other parameters set to their defaults. The 30 tasks
used for prompt optimization (all tasks except the 3 held out tasks) were split with 70% of tasks in the training set
and a 30% of the tasks in the validation set. With this split, the task involving construction of the local geometric
stiffness matrix was included in the training set. In our implementation, we use the prompt generated by the FEMbench 2025 as presented in Listing 3 for the coding task as the input to the optimizer, and the reﬂection stage uses the
respective reference function implemented in the task to give feedback to the reﬂecting LLM. In the GEPA optimizer
the mutation side of the genetic algorithm is handled by the reﬂection model. The reﬂection model is an LLM tasked
with performing implicit credit assignment to the candidate prompts, diagnosing their issues, and outputting a revised,
prompt instruction to ﬁx those issues. The reﬂection model in the GEPA optimizer can be different from the LLM
used to generate the task codes or tests. However, a study by Pandey et al. Pandey et al. [2026] suggests that prompts
optimized by a reﬂection LLM from the same model family as the code generation LLM result in better performance.
Here we only tested gemini-3-pro-preview and gpt-5 as the reﬂection model using the default reasoning effort
parameter across three GEPA optimization budgets: “light”, “medium”, and “heavy”. The budget controls how many
reﬂection and reﬁnement iterations GEPA is allowed to perform during optimization, with higher budgets enabling
more rounds of prompt evolution at the cost of additional LLM calls. The speciﬁc iteration counts associated with
each budget are reported in Table 9.
Table 9 shows that system prompts produced under the “heavy” optimization budget enabled both models to solve all
three tiers of the task. The resulting prompts are provided in Listings 6 and 7. In contrast, the “light” and “medium”
optimization budgets applied to gemini-3-pro-preview yielded no consistent improvement over the baseline (no
system prompt). Under these settings, GEPA consistently collapsed to overly generic prompts, shown in Listing 5,
which offered no task-speciﬁc guidance, particularly regarding construction of the local geometric stiffness matrix, a
component already identiﬁed as challenging in Table 3. A similar pattern occurred for GPT-5 under the “light” budget,
which also failed to solve Tier 3. However, unlike gemini-3-pro-preview, GPT-5 beneﬁted from both the “medium”
and “heavy” budgets and successfully completed Tier 3 in both cases. Overall, these results suggest that GEPA did not
yield any broadly applicable, domain-agnostic prompt improvements, and that meaningful gains arose only when the
optimized prompts incorporated substantial domain-speciﬁc knowledge.
Listing 5: GEPA optimized system prompt with “light” budget using gemini-3-pro-preview
Solve the problem and provide the answer in the correct format.

Listing 6: GEPA optimized system prompt with “heavy” budget using gemini-3-pro-preview

Table 9: Function correctness out of 5 runs on MSA_3D_elastic_critical_load task
MSA_3D_elastic_critical_load

Tier 1

Tier 2

Tier 3

Gemini 3 pro preview
No system prompt
Light (416 iterations)
Medium (735 iterations)
Heavy (1098 iterations)
No system prompt
Light (416 iterations)
Medium (735 iterations)
Heavy (1098 iterations)

You are an expert Python programmer specialized in Computational Structural Mechanics and Matrix
Structural Analysis (MSA). Your task is to implement specific Python functions for 3D beam element
analysis, exactly matching the provided function signatures and docstrings.
Follow these strict guidelines and domain-specific technical details:
### 1. Output Format
-**Code Only:** Return *only* the valid Python function definition. Do not include markdown blocks
(‘‘‘python ... ‘‘‘), comments outside the code, explanations, or imports that are not requested.
-**Self-Containment:** If the function requires logic for transformation matrices, elastic stiffness,
or load calculations, and those helper functions are *not* provided in the "Available Helper
Functions" section, you must define them as private inner functions (e.g., ‘def
_beam_transformation_matrix_3D(...)‘) within the scope of the main function.
### 2. Domain Knowledge: Geometric Stiffness Matrix ($k_g$)
When implementing geometric stiffness (often named with ‘CC1‘, ‘H0‘, ‘T0‘, ‘H4‘, ‘T3‘ suffixes), do not
derive coefficients from general textbooks, as sign conventions vary. Use the following **specific
formulation** for a 12x12 symmetric local geometric stiffness matrix.
**Variables:**
-‘L‘: Length
-‘Fx2‘: Axial force at node 2 (Tension +)
-‘Mx2‘: Torque at node 2
-‘My1‘, ‘My2‘: Bending moments about local y-axis at nodes 1 and 2
-‘Mz1‘, ‘Mz2‘: Bending moments about local z-axis at nodes 1 and 2
-‘I_rho‘: Polar moment of inertia ($I_x$ or $J$ depending on context, often $I_y + I_z$).
-‘A‘: Area
**Upper Triangle Coefficients (Indices 0-11):**
* ‘k[0, 6] = -Fx2 / L‘
* ‘k[1, 3] = My1 / L‘
* ‘k[1, 4] = Mx2 / L‘
* ‘k[1, 5] = Fx2 / 10.0‘
* ‘k[1, 7] = -6.0 * Fx2 / (5.0 * L)‘
* ‘k[1, 9] = My2 / L‘
* ‘k[1, 10] = -Mx2 / L‘
* ‘k[1, 11] = Fx2 / 10.0‘
* ‘k[2, 3] = Mz1 / L‘
* ‘k[2, 4] = -Fx2 / 10.0‘
* ‘k[2, 5] = Mx2 / L‘
* ‘k[2, 8] = -6.0 * Fx2 / (5.0 * L)‘
* ‘k[2, 9] = Mz2 / L‘
* ‘k[2, 10] = -Fx2 / 10.0‘
* ‘k[2, 11] = -Mx2 / L‘

* ‘k[3, 4] = -(2.0 * Mz1 -Mz2) / 6.0‘
* ‘k[3, 5] = (2.0 * My1 -My2) / 6.0‘
* ‘k[3, 7] = -My1 / L‘
* ‘k[3, 8] = -Mz1 / L‘
* ‘k[3, 9] = -Fx2 * I_rho / (A * L)‘ (Wagner term)
* ‘k[3, 10] = -(Mz1 + Mz2) / 6.0‘
* ‘k[3, 11] = (My1 + My2) / 6.0‘
* ‘k[4, 7] = -Mx2 / L‘
* ‘k[4, 8] = Fx2 / 10.0‘
* ‘k[4, 9] = -(Mz1 + Mz2) / 6.0‘
* ‘k[4, 10] = -Fx2 * L / 30.0‘
* ‘k[4, 11] = Mx2 / 2.0‘
* ‘k[5, 7] = -Fx2 / 10.0‘
* ‘k[5, 8] = -Mx2 / L‘
* ‘k[5, 9] = (My1 + My2) / 6.0‘
* ‘k[5, 10] = -Mx2 / 2.0‘
* ‘k[5, 11] = -Fx2 * L / 30.0‘
* ‘k[7, 9] = -My2 / L‘
* ‘k[7, 10] = Mx2 / L‘
* ‘k[7, 11] = -Fx2 / 10.0‘
* ‘k[8, 9] = -Mz2 / L‘
* ‘k[8, 10] = Fx2 / 10.0‘
* ‘k[8, 11] = Mx2 / L‘
* ‘k[9, 10] = (Mz1 -2.0 * Mz2) / 6.0‘
* ‘k[9, 11] = -(My1 -2.0 * My2) / 6.0‘
**Diagonal Terms:**
* ‘k[0, 0] = k[6, 6] = Fx2 / L‘
* ‘k[1, 1] = k[7, 7] = k[2, 2] = k[8, 8] = 6.0 * Fx2 / (5.0 * L)‘
* ‘k[3, 3] = k[9, 9] = Fx2 * I_rho / (A * L)‘
* ‘k[4, 4] = k[5, 5] = k[10, 10] = k[11, 11] = 2.0 * Fx2 * L / 15.0‘
**Construction:**
Initialize with zeros, apply upper triangle terms, add transpose (to symmetrize), then apply diagonal
terms (since diagonal terms were not set in the upper triangle step).
### 3. Implementation Strategy for Assembly Tasks
If asked to assemble a global geometric stiffness matrix (‘assemble_global_geometric_stiffness...‘):
1. **Iterate** through elements.
2. **Calculate Geometry:** Compute Length (‘L‘) and the Transformation Matrix (‘Gamma‘). If no
reference vector (‘local_z‘) is provided, default to Global Z, unless the beam is vertical
(parallel to Z), then use Global Y.
3. **Calculate Internal Forces:**
* Extract global displacements for the element nodes.
* Transform to local displacements: $u_{local} = Γ\cdot u_{global}$.
* Calculate **local elastic stiffness** ($k_e$).
* Compute local forces: $f_{local} = k_e \cdot u_{local}$.
* Extract ‘Fx2‘ (index 6), ‘Mx2‘ (index 9), ‘My1‘, ‘Mz1‘, ‘My2‘, ‘Mz2‘ (indices 4, 5, 10, 11) from
$f_{local}$.
4. **Compute Geometric Stiffness:** Pass these forces into the local geometric stiffness logic ($k_g$)
defined in Section 2.
5. **Globalize and Assemble:** $K_{g,global} = Γ^T \cdot k_g \cdot Γ$. Add to the global system matrix.
### 4. Constants & Helper Logic
-**Elastic Stiffness ($k_e$):**
-Axial: $EA/L$ at indices (0,0), etc.
-Torsion: $GJ/L$ at (3,3), etc.
-Bending: $12EI/L^3$, $6EI/L^2$, $4EI/L$, $2EI/L$.
-**Transformation Matrix ($Γ$):**
-Use direction cosines.
-$Γ$ is a 12x12 block diagonal matrix composed of four 3x3 rotation matrices.

Listing 7: GEPA optimized system prompt with “heavy” budget using gpt-5
You will receive Python function implementation tasks with strict formatting and domain-specific
requirements. Follow these instructions precisely to ensure your solution is accepted.
General rules for all tasks
-Output only valid Python code containing the single function requested. Do not include any
explanations, comments, assertions, prints, or markdown.
-Keep the function name, signature (including type hints), and docstring exactly as provided. Do not
alter spacing, order, or wording inside the docstring.
-Do not add any code outside the function body.
-Use only the imports explicitly listed in the task prompt. Do not import anything else. If imports are
allowed, place them inside the function unless told otherwise.
-Use only the helper functions explicitly provided in the prompt. Do not re-implement or modify them
unless the prompt explicitly states that helper functions are unavailable. If no helpers are
available, implement all needed logic inside the single function.
Coordinate systems, DOF ordering, and transformations (3D beam/frame tasks)
-Local element DOF ordering is always:
[u1, v1, w1, θx1, θy1, θz1, u2, v2, w2, θx2, θy2, θz2]
-Internal force vector (local) uses the same order mapped to force/moment resultants:
[Fx_i, Fy_i, Fz_i, Mx_i, My_i, Mz_i, Fx_j, Fy_j, Fz_j, Mx_j, My_j, Mz_j]
-The 12x12 transformation matrix Γrelates local and global systems via:
K_global = Γ.T @ K_local @ Γ
Therefore:
-Displacements transform to local with u_local = Γ@ u_global
-Forces transform to local with f_local = Γ.T @ f_global
-The 12x12 Γis composed of four repeated 3x3 direction cosine blocks along the diagonal, built from a
right-handed orthonormal triad (ex, ey, ez) where:
-ex is the unit vector along the element axis from node i to node j
-ey = normalize(cross(ref_vec, ex))
-ez = cross(ex, ey)
-If ref_vec (local_z) is not provided: use global z unless ex is nearly parallel to global z, then
use global y.
-Validate ref_vec when provided: shape (3,), unit length, and not parallel to ex.
-A zero-length element must raise an error in the transformation routine.
Local elastic stiffness of a 3D Euler-Bernoulli beam (when helpers are not provided)
-Use the standard 12x12 formulation with axial, torsional, and bending about local y and z:
-Axial: EA/L coupling u1-u2
-Torsion: GJ/L coupling θx1-θx2 with G = E/(2(1+ν))
-Bending about z (affects v and θz) uses E*Iz
-Bending about y (affects w and θy) uses E*Iy
-A canonical implementation (matching typical helpers) is:
k = np.zeros((12, 12))
EA_L = E * A / L
GJ_L = E * J / (2.0 * (1.0 + nu) * L)
EIz_L = E * Iz
EIy_L = E * Iy
# axial
k[0, 0] = k[6, 6] = EA_L
k[0, 6] = k[6, 0] = -EA_L
# torsion
k[3, 3] = k[9, 9] = GJ_L
k[3, 9] = k[9, 3] = -GJ_L
# bending about z (local y-displacements \& rotations about z)
k[1, 1] = k[7, 7] = 12.0 * EIz_L / L**3
k[1, 7] = k[7, 1] = -12.0 * EIz_L / L**3
k[1, 5] = k[5, 1] = k[1, 11] = k[11, 1] = 6.0 * EIz_L / L**2
k[5, 7] = k[7, 5] = k[7, 11] = k[11, 7] = -6.0 * EIz_L / L**2
k[5, 5] = k[11, 11] = 4.0 * EIz_L / L
k[5, 11] = k[11, 5] = 2.0 * EIz_L / L
# bending about y (local z-displacements \& rotations about y)
k[2, 2] = k[8, 8] = 12.0 * EIy_L / L**3

k[2, 8] = k[8, 2] = -12.0 * EIy_L / L**3
k[2, 4] = k[4, 2] = k[2, 10] = k[10, 2] = -6.0 * EIy_L / L**2
k[4, 8] = k[8, 4] = k[8, 10] = k[10, 8] = 6.0 * EIy_L / L**2
k[4, 4] = k[10, 10] = 4.0 * EIy_L / L
k[4, 10] = k[10, 4] = 2.0 * EIy_L / L
Computing internal element end forces (local)
-Given global element displacements u_dofs_global of length 12 and geometry:
1) Build Γwith the transformation routine.
2) Compute element length L = ||xj -xi||.
3) Build the local elastic stiffness k_e_local as above or via provided helper.
4) Transform displacements to local: u_local = Γ@ u_dofs_global.
5) Internal end forces (local) are load_local = k_e_local @ u_local.
Local geometric stiffness matrix with torsion-bending coupling (12x12)
-For the function MSA_3D_local_geometric_stiffness_CC1_H0_T0, you must construct the full consistent
local geometric (initial-stress) stiffness with coupling between axial force Fx2, torsion Mx2, and
end bending moments My1, Mz1, My2, Mz2, including polar inertia coupling via I_rho and A. Use
exactly this formulation:
k_g = np.zeros((12, 12))
# upper triangle off diagonal terms
k_g[0, 6] = -Fx2 / L
k_g[1, 3] = My1 / L
k_g[1, 4] = Mx2 / L
k_g[1, 5] = Fx2 / 10.0
k_g[1, 7] = -6.0 * Fx2 / (5.0 * L)
k_g[1, 9] = My2 / L
k_g[1, 10] = -Mx2 / L
k_g[1, 11] = Fx2 / 10.0
k_g[2, 3] = Mz1 / L
k_g[2, 4] = -Fx2 / 10.0
k_g[2, 5] = Mx2 / L
k_g[2, 8] = -6.0 * Fx2 / (5.0 * L)
k_g[2, 9] = Mz2 / L
k_g[2, 10] = -Fx2 / 10.0
k_g[2, 11] = -Mx2 / L
k_g[3, 4] = -1.0 * (2.0 * Mz1 -Mz2) / 6.0
k_g[3, 5] = (2.0 * My1 -My2) / 6.0
k_g[3, 7] = -My1 / L
k_g[3, 8] = -Mz1 / L
k_g[3, 9] = -Fx2 * I_rho / (A * L)
k_g[3, 10] = -1.0 * (Mz1 + Mz2) / 6.0
k_g[3, 11] = (My1 + My2) / 6.0
k_g[4, 7] = -Mx2 / L
k_g[4, 8] = Fx2 / 10.0
k_g[4, 9] = -1.0 * (Mz1 + Mz2) / 6.0
k_g[4, 10] = -Fx2 * L / 30.0
k_g[4, 11] = Mx2 / 2.0
k_g[5, 7] = -Fx2 / 10.0
k_g[5, 8] = -Mx2 / L
k_g[5, 9] = (My1 + My2) / 6.0
k_g[5, 10] = -Mx2 / 2.0
k_g[5, 11] = -Fx2 * L / 30.0
k_g[7, 9] = -My2 / L
k_g[7, 10] = Mx2 / L
k_g[7, 11] = -Fx2 / 10.0
k_g[8, 9] = -Mz2 / L
k_g[8, 10] = Fx2 / 10.0
k_g[8, 11] = Mx2 / L
k_g[9, 10] = (Mz1 -2.0 * Mz2) / 6.0
k_g[9, 11] = -1.0 * (My1 -2.0 * My2) / 6.0
# add in the symmetric lower triangle
k_g = k_g + k_g.transpose()
# add diagonal terms

k_g[0, 0] = Fx2 / L
k_g[1, 1] = 6.0 * Fx2 / (5.0 * L)
k_g[2, 2] = 6.0 * Fx2 / (5.0 * L)
k_g[3, 3] = Fx2 * I_rho / (A * L)
k_g[4, 4] = 2.0 * Fx2 * L / 15.0
k_g[5, 5] = 2.0 * Fx2 * L / 15.0
k_g[6, 6] = Fx2 / L
k_g[7, 7] = 6.0 * Fx2 / (5.0 * L)
k_g[8, 8] = 6.0 * Fx2 / (5.0 * L)
k_g[9, 9] = Fx2 * I_rho / (A * L)
k_g[10, 10] = 2.0 * Fx2 * L / 15.0
k_g[11, 11] = 2.0 * Fx2 * L / 15.0
Global geometric stiffness assembly (when required)
-Global DOFs per node are 6, ordered [u_x, u_y, u_z, θ_x, θ_y, θ_z].
-For each element:
1) Determine node indices ni, nj and their coordinates.
2) Build Γand element length L.
3) Extract the element’s global displacement subvector u_e (12x1).
4) Transform to local: d_loc = Γ@ u_e.
5) Compute local elastic stiffness k_el (as above or via helper).
6) Compute internal local end forces: f_loc = k_el @ d_loc.
7) Extract geometric parameters from f_loc for k_g^local construction:
Fx2 = f_loc[6]
Mx2 = f_loc[9]
My1 = f_loc[4]
Mz1 = f_loc[5]
My2 = f_loc[10]
Mz2 = f_loc[11]
8) Build k_g_local using the exact 12x12 formulation above.
9) Transform to global: k_g_global = Γ.T @ k_g_local @ Γ.
10) Assemble into the global matrix K at the element’s DOF indices.
-After assembly, you may enforce symmetry via K = 0.5 * (K + K.T) to counter minor numerical
asymmetries.
Common pitfalls to avoid
-Do not use Γ.T to transform displacements; the correct is u_local = Γ@ u_global.
-Respect the exact DOF ordering and index mapping when extracting forces and moments.
-Do not omit torsion-bending and moment-displacement/rotation coupling terms in geometric stiffness;
use the full matrix provided above when requested.
-Do not add extra imports or code outside the function.
-Ensure no extraneous output (no prints, comments, or markdown).
When in doubt, strictly follow the formulas and conventions above; these reflect the expected answers
for these tasks.

Inspection of the code produced by LLMs for Tier 3 of the MSA_3D_elastic_critical_load task shows that the
models consistently struggled to construct the local geometric stiffness matrix, a core requirement of the problem. The
contrast between their success on Tier 2 and failure on Tier 3 reinforces this observation. A similar limitation appears
in the GEPA-optimized prompts, which ultimately needed to provide the geometric stiffness matrix explicitly for the
models to succeed. Taken together, these results indicate that even when LLMs can handle broader tasks with ease,
they are unable to solve specialized and technically intricate problems without access to essential domain knowledge.
In this particular case, the models were not able to recall or derive the local geometric stiffness matrix on the ﬂy, but
once that information was supplied through tools or system context they became capable of solving substantially more
complex challenges.
While the current system prompt is effective for completing the hardest task in the FEM-Bench 2025 suite, it is
unlikely to generalize to areas of FEM or MSA that fall outside the present scope, such as elasto-plasticity or dynamic
analysis. Achieving broad generalizability across these domains may require fundamental advances in an LLMs ability
to synthesize information from multiple sources and reason over heterogeneous technical inputs. This is precisely
where AI agents equipped with multiple external tools may become valuable. Looking ahead, we anticipate that

integrating capabilities such as symbolic reasoning, automated code execution, and authoritative retrieval will be
essential for enabling LLMs to move beyond prior accessible domain knowledge for solving FEM related tasks.

References
Anton Bakhtin, Laurens van der Maaten, Justin Johnson, Laura Gustafson, and Ross Girshick. Phyre: A new benchmark for physical reasoning. Advances in Neural Information Processing Systems, 32, 2019.
Yi Wang, Jiafei Duan, Dieter Fox, and Siddhartha Srinivasa. Newton: Are large language models capable of physical
reasoning? In Findings of the association for computational linguistics: EMNLP 2023, pages 9743–9758, 2023.
Hao Cui, Zahra Shamsi, Gowoon Cheon, Xuejian Ma, Shutong Li, Maria Tikhanovskaya, Peter Norgaard, Nayantara
Mudur, Martyna Plomecka, Paul Raccuglia, et al. Curie: Evaluating llms on multitask scientiﬁc long context
understanding and reasoning. arXiv preprint arXiv:2503.13517, 2025.
Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang,
Carrie Cai, Michael Terry, Quoc Le, et al. Program synthesis with large language models. arXiv preprint
arXiv:2108.07732, 2021a.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards,
Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy
Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power,
Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings,
Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol,
Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher
Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight,
Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya
Sutskever, and Wojciech Zaremba. Evaluating large language models trained on code. 2021a.
Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Oﬁr Press, and Karthik Narasimhan. Swebench: Can language models resolve real-world github issues? arXiv preprint arXiv:2310.06770, 2023.
Elliot Glazer, Ege Erdil, Tamay Besiroglu, Diego Chicharro, Evan Chen, Alex Gunning, Caroline Falkman Olsson,
Jean-Stanislas Denain, Anson Ho, Emily de Oliveira Santos, et al. Frontiermath: A benchmark for evaluating
advanced mathematical reasoning in ai. arXiv preprint arXiv:2411.04872, 2024.
Minyang Tian, Luyu Gao, Shizhuo Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas, Pan Ji, Kittithat
Krongchon, Yao Li, et al. Scicode: A research coding benchmark curated by scientists. Advances in Neural
Information Processing Systems, 37:30624–30650, 2024.
Qile Jiang, Zhiwei Gao, and George Em Karniadakis. Deepseek vs. chatgpt vs. claude: A comparative study for
scientiﬁc computing and scientiﬁc machine learning tasks. Theoretical and Applied Mechanics Letters, 15(3):
100583, 2025.
Weicheng Huang, Xiaonan Huang, Carmel Majidi, and M Khalid Jawed. Dynamic simulation of articulated soft robots.
Nature communications, 11(1):2233, 2020.
Steven A Niederer, Michael S Sacks, Mark Girolami, and Karen Willcox. Scaling digital twins from the artisanal to
the industrial. Nature Computational Science, 1(5):313–320, 2021.
Gokhan Danabasoglu, J-F Lamarque, J Bacmeister, DA Bailey, AK DuVivier, Jim Edwards, LK Emmons, John Fasullo, R Garcia, Andrew Gettelman, et al. The community earth system model version 2 (cesm2). Journal of
Advances in Modeling Earth Systems, 12(2):e2019MS001916, 2020.
Cameron Talischi, Glaucio H Paulino, Anderson Pereira, and Ivan FM Menezes. Polytop: a matlab implementation
of a general topology optimization framework using unstructured polygonal ﬁnite element meshes. Structural and
Multidisciplinary Optimization, 45(3):329–357, 2012.
Roger D Peng. Reproducible research in computational science. Science, 334(6060):1226–1227, 2011.
William L Oberkampf and Christopher J Roy. Veriﬁcation and validation in scientiﬁc computing. Cambridge university
press, 2010.
Daniel Arndt, Wolfgang Bangerth, Maximilian Bergbauer, Marco Feder, Marc Fehling, Johannes Heinz, Timo Heister,
Luca Heltai, Martin Kronbichler, Matthias Maier, et al. The deal. ii library, version 9.5. Journal of Numerical
Mathematics, 31(3):231–246, 2023.
Martin Alnæs, Jan Blechta, Johan Hake, August Johansson, Benjamin Kehlet, Anders Logg, Chris Richardson, Johannes Ring, Marie E Rognes, and Garth N Wells. The fenics project version 1.5. Archive of numerical software, 3
(100), 2015.

Richard Courant et al. Variational methods for the solution of problems of equilibrium and vibrations. Lecture notes
in pure and applied mathematics, pages 1–1, 1994.
M Jon Turner, Ray W Clough, Harold C Martin, and LJ Topp. Stiffness and deﬂection analysis of complex structures.
journal of the Aeronautical Sciences, 23(9):805–823, 1956.
OC Zienkiewicz and Richard Lawrence Taylor. The ﬁnite element patch test revisited a computer test for convergence,
validation and error estimates. Computer methods in applied mechanics and engineering, 149(1-4):223–254, 1997.
Thomas JR Hughes. The ﬁnite element method: linear static and dynamic ﬁnite element analysis. Courier Corporation,
2003.
Krishna Garikipati. The ﬁnite element method for problems in physics. Coursera [MOOC], 2015. URL https:
//www.coursera.org/learn/finite-element-method.
Mostafa Faghih Shojaei, Rahul Gulati, Benjamin A Jasperson, Shangshang Wang, Simone Cimolato, Dangli Cao,
Willie Neiswanger, and Krishna Garikipati. Ai-university: An llm-based platform for instructional alignment to
scientiﬁc classrooms. arXiv preprint arXiv:2504.08846, 2025.
Farhad Kamarei, Bo Zeng, John E Dolbow, and Oscar Lopez-Pamies. Nine circles of elastic brittle fracture: A series
of challenge problems to assess fracture models. Computer Methods in Applied Mechanics and Engineering, 448:
118449, 2026.
Barna Szabó and Ivo Babuška. Finite element analysis: Method, veriﬁcation and validation. 2021.
Ted Belytschko, Wing Kam Liu, Brian Moran, and Khalil Elkhodary. Nonlinear ﬁnite elements for continua and
structures. John wiley & sons, 2014.
Morton E Gurtin, Eliot Fried, and Lallit Anand. The mechanics and thermodynamics of continua. Cambridge university press, 2010.
Hans Petter Langtangen. Computational partial differential equations: numerical methods and diffpack programming,
volume 2. Springer Berlin, 2003.
William McGuire, Richard H Gallagher, and Ronald D Ziemian. Matrix structural analysis. 2000.
John H Argyris, Sydney Kelsey, et al. Energy theorems and structural analysis, volume 60. Springer, 1960.
Robert D Cook et al. Concepts and applications of ﬁnite element analysis. John wiley & sons, 2007.
Carlos A Felippa. Introduction to ﬁnite element methods. 2004.
Gilbert Strang, George J Fix, et al. An analysis of the ﬁnite element method, volume 212. Prentice-hall, 1973.
William H Press. Numerical recipes 3rd edition: The art of scientiﬁc computing. Cambridge university press, 2007.
Klaus Jurgen Bathe. Finite element procedures, 1996.
J Austin Cottrell, Thomas JR Hughes, and Yuri Bazilevs. Isogeometric analysis: toward integration of CAD and FEA.
John Wiley & Sons, 2009.
Nicholas J Higham. Accuracy and stability of numerical algorithms. SIAM, 2002.
Gerhard A Holzapfel. Nonlinear solid mechanics: a continuum approach for engineering science, 2002.
Richard H Macneal and Robert L Harder. A proposed standard set of problems to test ﬁnite element accuracy. Finite
elements in analysis and design, 1(1):3–20, 1985.
Patrick J Roache. Veriﬁcation and validation in computational science and engineering, volume 895. Hermosa Albuquerque, NM, 1998.
Paul Ammann and Jeff Offutt. Introduction to software testing. Cambridge University Press, 2017.
James D Foley. Computer graphics: principles and practice, volume 12110. Addison-Wesley Professional, 1996.
Lloyd N Trefethen and David Bau. Numerical linear algebra. SIAM, 2022.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards,
Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy
Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power,
Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings,
Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol,
Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher
Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight,
Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya
Sutskever, and Wojciech Zaremba. Evaluating large language models trained on code, 2021b. URL https://
arxiv.org/abs/2107.03374.

Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang,
Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. Program synthesis with large language models, 2021b.
URL https://arxiv.org/abs/2108.07732.
Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Oﬁr Press, and Karthik R Narasimhan.
SWE-bench: Can language models resolve real-world github issues? In The Twelfth International Conference on
Learning Representations, 2024. URL https://openreview.net/forum?id=VTF8yNQM66.
Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang, Ruiqi Zhong, Luke Zettlemoyer, Scott Wen tau Yih, Daniel
Fried, Sida Wang, and Tao Yu. Ds-1000: A natural and reliable benchmark for data science code generation. ArXiv,
abs/2211.11501, 2022.
Erfan Hamdi and Emma Lejeune. Towards robust surrogate models: Benchmarking machine learning approaches to
expediting phase ﬁeld simulations of brittle fracture. Computer Methods in Applied Mechanics and Engineering,
449:118526, 2026.
Emma Lejeune. Mechanical mnist: A benchmark dataset for mechanical metamodels. Extreme Mechanics Letters,
36:100659, 2020.
Joel Shor, Erik Strand, and Cory Y. McLean. Nucleobench: A large-scale benchmark of neural nucleic acid design
algorithms. bioRxiv, 2025. doi:10.1101/2025.06.20.660785. URL https://www.biorxiv.org/content/early/
2025/08/26/2025.06.20.660785. Presented at the ICML 2025 GenBio Workshop.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. NeurIPS, 2021.
Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar. Gsmsymbolic: Understanding the limitations of mathematical reasoning in large language models, 2025. URL https:
//arxiv.org/abs/2410.05229.
Rushikesh Deotale, Adithya Srinivasan, Mahmoud Golestanian, Yuan Tian, Tianyi Zhang, Pavlos Vlachos, and Hector
Gomez. All-fem: Agentic large language models ﬁne-tuned for ﬁnite element methods. Computer Methods in
Applied Mechanics and Engineering, 457:118985, 2026.
Nayantara Mudur, Hao Cui, Subhashini Venugopalan, Paul Raccuglia, Michael Brenner, and Peter Christian Norgaard.
Feabench: Evaluating language models on real world physics reasoning ability. 2024.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang,
Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of language models. arXiv preprint
arXiv:2211.09110, 2022.
Bowen Jiang, Yangxinyu Xie, Zhuoqun Hao, Xiaomeng Wang, Tanwi Mallick, Weijie J Su, Camillo Jose Taylor, and
Dan Roth. A peek into token bias: Large language models are not yet genuine reasoners. In Proceedings of the
2024 Conference on Empirical Methods in Natural Language Processing, pages 4722–4756, 2024.
Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H Chi, Nathanael Schärli, and Denny
Zhou. Large language models can be easily distracted by irrelevant context. In International Conference on Machine
Learning, pages 31210–31227. PMLR, 2023.
Gustavo Pinto, Cleidson De Souza, João Batista Neto, Alberto Souza, Tarcísio Gotto, and Edward Monteiro. Lessons
from building stackspot ai: A contextualized ai coding assistant. In Proceedings of the 46th International Conference
on Software Engineering: Software Engineering in Practice, pages 408–417, 2024.
Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix
Weissenberger, Keran Rong, Ryutaro Tanno, et al. Towards an ai co-scientist. arXiv preprint arXiv:2502.18864,
2025.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini
Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback.
Advances in neural information processing systems, 35:27730–27744, 2022.
Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. Pre-train, prompt, and
predict: A systematic survey of prompting methods in natural language processing. ACM computing surveys, 55
(9):1–35, 2023.
Zhen Hang, Yushan Yashengjiang, Junhui Li, Huanshuo Dong, Yang Wei, Zhezheng Hao, Jiangtao Ma, Songlin
Bai, Haozhong Kai, Xihang Yue, et al. Pdeagent-bench: A multi-metric, multi-library benchmark for pde solver
generation. arXiv preprint arXiv:2605.09636, 2026.
Hengxing Cai, Xiaochen Cai, Junhan Chang, Sihang Li, Lin Yao, Wang Changxin, Zhifeng Gao, Hongshuai Wang,
Li Yongge, Mujie Lin, et al. Sciassess: Benchmarking llm proﬁciency in scientiﬁc literature analysis. In Findings
of the Association for Computational Linguistics: NAACL 2025, pages 2335–2357, 2025.

Parshin Shojaee, Ngoc-Hieu Nguyen, Kazem Meidani, Amir Barati Farimani, Khoa D Doan, and Chandan K Reddy.
Llm-srbench: A new benchmark for scientiﬁc equation discovery with large language models. arXiv preprint
arXiv:2504.10415, 2025.
Zhangde Song, Jieyu Lu, Yuanqi Du, Botao Yu, Thomas M Pruyn, Yue Huang, Kehan Guo, Xiuzhe Luo, Yuanhao Qu,
Yi Qu, et al. Evaluating large language models in scientiﬁc discovery. arXiv preprint arXiv:2512.15567, 2025.
Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, and Pengfei Liu. Evaluating mathematical reasoning beyond
accuracy. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence, volume 39, pages 27723–27730, 2025.
Shibo Hao, Yi Gu, Haotian Luo, Tianyang Liu, Xiyan Shao, Xinyuan Wang, Shuhua Xie, Haodi Ma, Adithya
Samavedhi, Qiyue Gao, et al. Llm reasoners: New evaluation, library, and analysis of step-by-step reasoning
with large language models. arXiv preprint arXiv:2404.05221, 2024.
Weixi Tong and Tianyi Zhang. Codejudge: Evaluating code generation with large language models. In Proceedings
of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 20032–20051, 2024.
Minglai Yang, Ethan Huang, Liang Zhang, Mihai Surdeanu, William Yang Wang, and Liangming Pan. How is llm
reasoning distracted by irrelevant context? an analysis using a controlled benchmark. In Proceedings of the 2025
Conference on Empirical Methods in Natural Language Processing, pages 13340–13358, 2025.
Olgierd C Zienkiewicz and Robert Leroy Taylor. The ﬁnite element method set. Elsevier, 2005.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan,
Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in neural
information processing systems, 33:1877–1901, 2020.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li,
Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv
preprint arXiv:2402.03300, 2024.
Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi,
Herumb Shandilya, Michael J Ryan, Meng Jiang, et al. Gepa: Reﬂective prompt evolution can outperform reinforcement learning. arXiv preprint arXiv:2507.19457, 2025.
Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, and Jimmy Ba.
Large language models are human-level prompt engineers. In The eleventh international conference on learning
representations, 2022.
Krista Opsahl-Ong, Michael J Ryan, Josh Purtell, David Broman, Christopher Potts, Matei Zaharia, and Omar
Khattab. Optimizing instructions and demonstrations for multi-stage language model programs. arXiv preprint
arXiv:2406.11695, 2024.
Qingyan Guo, Rui Wang, Junliang Guo, Bei Li, Kaitao Song, Xu Tan, Guoqing Liu, Jiang Bian, and Yujiu Yang.
Connecting large language models with evolutionary algorithms yields powerful prompt optimizers. arXiv preprint
arXiv:2309.08532, 2023.
Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful
Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, and Christopher Potts.
Dspy: Compiling declarative language model calls into self-improving pipelines. 2024.
Omar Khattab, Keshav Santhanam, Xiang Lisa Li, David Hall, Percy Liang, Christopher Potts, and Matei Zaharia.
Demonstrate-search-predict: Composing retrieval and language models for knowledge-intensive NLP. arXiv
preprint arXiv:2212.14024, 2022.
Rohan Pandey, Eric Ye, and Michael Li. Beyond the answer: Decoding the behavior of llms as scientiﬁc reasoners.
arXiv preprint arXiv:2603.28038, 2026.
