Summary:	A Semantic Web Framework for Java
Summary(pl):	Szkielet semantyczny WWW dla Javy
Name:		jena
Version:	2.1
Release:	0.1
License:	hp
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/jena/Jena-%{version}.zip
# Source0-md5:	a0f9cbcb060473cf8eb348cdf703d7d8
URL:		http://jade.tilab.com/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	unzip
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jena is Java toolkit for developing semantic web applications based on
W3C recommendations for RDF and OWL. It provides an RDF API; ARP, an
RDF parser; RDQL, an RDF query language; an OWL API; and rule-based
inference for RDFS and OWL.

%description -l pl
Jena to zbiór narzêdzi Javy do tworzenia aplikacji semantycznych WWW
opartych na rekomendacjach W3C dla RDF i OWL. Udostêpnia: API RDF,
ARP - analizator RDF, RDQL - jêzyk zapytañ RDF, API OWL oraz oparte na
regu³ach wnioskowanie dla RDFS i OWL.

# TODO:
#%package doc
#Summary:	Online manual for jade
#Summary(pl):	Dokumentacja online do jade
#Group:		Documentation

#%description doc

%prep
%setup -q -n Jena-%{version}

%build
ant jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}/%{name}}

install lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.html
%{_javadir}/%{name}

#%files doc
#%defattr(644,root,root,755)
#%doc docs
