%global packname  latticist
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.44
Release:          1
Summary:          A graphical user interface for exploratory visualisation
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/latticist_0.9-44.tar.gz
Requires:         R-lattice R-latticeExtra R-vcd R-gWidgets R-utils
Requires:         R-playwith R-hexbin R-deldir R-tripack R-DAAG R-RGtk2
Requires:         R-gWidgetsRGtk2 R-gWidgetstcltk R-MASS
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-lattice R-latticeExtra R-vcd R-gWidgets R-utils
BuildRequires:    R-playwith R-hexbin R-deldir R-tripack R-DAAG R-RGtk2
BuildRequires:    R-gWidgetsRGtk2 R-gWidgetstcltk R-MASS

%description
Latticist provides a graphical user interface for exploratory
visualisation. It is primarily an interface to the Lattice graphics
system, but also produces displays from the vcd package for categorical
data. Given a multivariate dataset (either a data frame or a table),
latticist attempts to produce useful displays based on the properties of
the data. The displays can be customised by editing the calls used to
generate them.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/help

