outdir=$(shell pwd)
spec=python-aspell.spec

srpm: $(spec)
	which spectool || dnf install -y spectool
	spectool -g $<
	rpmbuild $< --bs --define "%_srcrpmdir $(outdir)" --define "%_sourcedir $$(pwd)"
