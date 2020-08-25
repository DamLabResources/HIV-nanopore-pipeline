import subprocess

# Chunk length is the same as used in the "align_reference_to_draft"
# rule in the alignment.snk file
feature_gen="""medaka features snakemake.input.calls2draft snakemake.output \
--truth snakemake.input.truth2draft \
--threads snakemake.threads \
--regions """

feature_gen += ' '.join([f"{ref}:0-{end}" for ref,end in zip(snakemake.params.refname, snakemake.params.train_end)])

feature_gen += """ --batch_size snakemake.params.batchsize \
--chunk_len snakemake.params.chunk_len \
--chunk_ovlp snakemake.params.chunk_ovlp \
dtypes=snakemake.params.genomes"""

subprocess.run(feature_gen, shell = True)

# feature_gen="""medaka features snakemake.input.calls2draft snakemake.output \
# --truth snakemake.input.truth2draft \
# --threads snakemake.threads \
# --regions """

# feature_gen += ' '.join([f"{ref}:0-{end}" for ref,end in zip(snakemake.params.refname, snakemake.params.train_end)])

# feature_gen += """ --batch_size snakemake.params.batchsize \
# --chunk_len snakemake.params.chunk_len \
# --chunk_ovlp snakemake.params.chunk_ovlp \
# dtypes=snakemake.params.genomes"""

# subprocess.run(feature_gen)