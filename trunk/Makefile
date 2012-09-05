OBSPACKAGE=supportutils-plugin-updater
SVNDIRS=specs scripts man
VERSION=$(shell awk '/Version:/ { print $$2 }' specs/${OBSPACKAGE}.spec)
RELEASE=$(shell awk '/Release:/ { print $$2 }' specs/${OBSPACKAGE}.spec)
SRCDIR=$(OBSPACKAGE)-$(VERSION)
SRCFILE=$(SRCDIR).tar
BUILDDIR=/usr/src/packages

default: build

install: dist
	@echo ==================================================================
	@echo Installing source files into build directory
	@echo ==================================================================
	cp src/$(SRCFILE).gz $(BUILDDIR)/SOURCES
	cp specs/$(OBSPACKAGE).spec $(BUILDDIR)/SPECS
	@echo

uninstall:
	@echo ==================================================================
	@echo Uninstalling from build directory
	@echo ==================================================================
	rm -rf $(BUILDDIR)/SOURCES/$(SRCFILE).gz
	rm -rf $(BUILDDIR)/SPECS/$(OBSPACKAGE).spec
	rm -rf $(BUILDDIR)/BUILD/$(SRCDIR)
	rm -f $(BUILDDIR)/SRPMS/$(OBSPACKAGE)-$(VERSION)-$(RELEASE).src.rpm
	rm -f $(BUILDDIR)/RPMS/noarch/$(OBSPACKAGE)-$(VERSION)-$(RELEASE).noarch.rpm
	@echo

dist:
	@echo ==================================================================
	@echo Creating distribution source tarball
	@echo ==================================================================
	mkdir -p $(SRCDIR)
	for i in $(SVNDIRS); do cp $$i/* $(SRCDIR); done
	cp COPYING.GPLv2 $(SRCDIR)
	tar cf $(SRCFILE) $(SRCDIR)/*
	gzip -9f $(SRCFILE)
	rm -rf $(SRCDIR)
	mv -f $(SRCFILE).gz src
	@echo

clean:
	@echo ==================================================================
	@echo Cleaning up make files
	@echo ==================================================================
	rm -rf $(OBSPACKAGE)*
	for i in $(SVNDIRS); do rm -f $$i/*~; done
	rm -f *~
	@echo

allclean: uninstall clean
	@echo
	@ls -al ${LS_OPTIONS}
	@echo

build: allclean install
	@echo ==================================================================
	@echo Building RPM package
	@echo ==================================================================
	rpmbuild -ba $(BUILDDIR)/SPECS/$(OBSPACKAGE).spec
	cp $(BUILDDIR)/SRPMS/$(OBSPACKAGE)-$(VERSION)-$(RELEASE).src.rpm .
	cp $(BUILDDIR)/RPMS/noarch/$(OBSPACKAGE)-$(VERSION)-$(RELEASE).noarch.rpm .
	@echo
	@ls -al ${LS_OPTIONS}
	@echo

buildci: allclean install
	@echo ==================================================================
	@echo Building RPM package
	@echo ==================================================================
	rpmbuild -ba $(BUILDDIR)/SPECS/$(OBSPACKAGE).spec
	cp $(BUILDDIR)/SRPMS/$(OBSPACKAGE)-$(VERSION)-$(RELEASE).src.rpm .
	cp $(BUILDDIR)/RPMS/noarch/$(OBSPACKAGE)-$(VERSION)-$(RELEASE).noarch.rpm .
	@echo
	svn up
	svn ci -m "Build SVN Check In: $(OBSPACKAGE)-$(VERSION)-$(RELEASE)"
	@ls -al ${LS_OPTIONS}
	@echo
	
commit: build
	@echo ==================================================================
	@echo Committing changes to OBS Novell:NTS/$(OBSPACKAGE)
	@echo ==================================================================
	osc up Novell:NTS/$(OBSPACKAGE)
	osc del Novell:NTS/$(OBSPACKAGE)/*
	osc ci -m "Removing old files before committing: $(OBSPACKAGE)-$(VERSION)-$(RELEASE)" Novell:NTS/$(OBSPACKAGE)
	@rm -f Novell:NTS/$(OBSPACKAGE)/*
	cp specs/$(OBSPACKAGE).spec Novell:NTS/$(OBSPACKAGE)
	cp src/$(SRCFILE).gz Novell:NTS/$(OBSPACKAGE)
	osc add Novell:NTS/$(OBSPACKAGE)/*
	osc up Novell:NTS/$(OBSPACKAGE)
	osc ci -m "Committing to OBS: $(OBSPACKAGE)-$(VERSION)-$(RELEASE)" Novell:NTS/$(OBSPACKAGE)
	svn up
	svn ci -m "Committed to OBS: $(OBSPACKAGE)-$(VERSION)-$(RELEASE)"
	@echo

obsetup:
	@echo ==================================================================
	@echo Setup OBS Novell:NTS/$(OBSPACKAGE)
	@echo ==================================================================
	@rm -rf Novell:NTS
	osc co Novell:NTS/$(OBSPACKAGE)
	@rm -f Novell:NTS/$(OBSPACKAGE)/*
	cp specs/$(OBSPACKAGE).spec Novell:NTS/$(OBSPACKAGE)
	cp src/$(SRCFILE).gz Novell:NTS/$(OBSPACKAGE)
	osc status Novell:NTS/$(OBSPACKAGE)

help:
	@clear
	@make -v
	@echo
	@echo Make options for package: $(OBSPACKAGE)
	@echo make {install, uninstall, dist, clean, allclean, build[default], buildci, obsetup, commit}
	@echo
