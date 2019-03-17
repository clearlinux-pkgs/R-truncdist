#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-truncdist
Version  : 1.0.2
Release  : 7
URL      : https://cran.r-project.org/src/contrib/truncdist_1.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/truncdist_1.0-2.tar.gz
Summary  : Truncated Random Variables
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-evd
BuildRequires : R-evd
BuildRequires : buildreq-R

%description
functions, cumulative distribution functions, quantile functions
        and random numbers for truncated random variables.  These functions are
        provided to also compute the expected value and variance. Nadarajah
        and Kotz (2006) developed most of the functions. QQ plots can be produced.
        All the probability functions in the stats, stats4 and evd
        packages are automatically available for truncation..

%prep
%setup -q -c -n truncdist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552802638

%install
export SOURCE_DATE_EPOCH=1552802638
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library truncdist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library truncdist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library truncdist
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  truncdist || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/truncdist/DESCRIPTION
/usr/lib64/R/library/truncdist/INDEX
/usr/lib64/R/library/truncdist/Meta/Rd.rds
/usr/lib64/R/library/truncdist/Meta/features.rds
/usr/lib64/R/library/truncdist/Meta/hsearch.rds
/usr/lib64/R/library/truncdist/Meta/links.rds
/usr/lib64/R/library/truncdist/Meta/nsInfo.rds
/usr/lib64/R/library/truncdist/Meta/package.rds
/usr/lib64/R/library/truncdist/NAMESPACE
/usr/lib64/R/library/truncdist/R/truncdist
/usr/lib64/R/library/truncdist/R/truncdist.rdb
/usr/lib64/R/library/truncdist/R/truncdist.rdx
/usr/lib64/R/library/truncdist/help/AnIndex
/usr/lib64/R/library/truncdist/help/aliases.rds
/usr/lib64/R/library/truncdist/help/paths.rds
/usr/lib64/R/library/truncdist/help/truncdist.rdb
/usr/lib64/R/library/truncdist/help/truncdist.rdx
/usr/lib64/R/library/truncdist/html/00Index.html
/usr/lib64/R/library/truncdist/html/R.css
