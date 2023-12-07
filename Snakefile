# a. prepare: runs prepare_data.py script
# b. profile: runs profile.py script
# c. analyze: runs analyze.py script


rule prepare:
    output:
        "data/csv/bank-additional/bank-additional-full.csv",
    shell:
        "python3 scripts/prepare_data.py"
rule profile:
    input:
        "data/csv/bank-additional/bank-additional-full.csv",
    output:
        "profiling/report.html"
    shell:
        "python3 scripts/profile.py"
rule analyze:
    input:
        "data/csv/bank-additional/bank-additional-full.csv",
    output:
        "results/summary.txt",
        "results/age_job.txt"
    shell:
        "python3 scripts/analysis.py"
