
configfile: "config.yaml"
report: "report/nanopore.rst"

rule run_pipeline:
    input:
        expand("medaka_pipeline_outputs/guppy/assembly/racon/medaka/{genomes}_consensus.fa",
                genomes = config["genomes"])

# nanopore consensus pipeline
include: "snakes/basecalling.snk"
include: "snakes/assembly.snk"
include: "snakes/racon.snk"
include: "snakes/consensus.snk"

# medaka feature generation pipeline
include: "snakes/alignment.snk"
include: "snakes/converge_HIV_reads.snk"
include: "snakes/medaka_train.snk"

# Evaluation
# include: "snakes/consensus_evaluation.snk"