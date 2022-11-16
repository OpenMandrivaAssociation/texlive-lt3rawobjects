Name:		texlive-lt3rawobjects
Version:	64038
Release:	1
Summary:	Objects and proxies in LaTeX3
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lt3rawobjects
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3rawobjects.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3rawobjects.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3rawobjects.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package introduces a new mechanism to create objects like
the well known C structures. The functions exported by this
package are quite low level, and many important mechanisms like
member protection and name resolution aren't already defined
and should be introduced by intermediate packages.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/lt3rawobjects
%{_texmfdistdir}/tex/latex/lt3rawobjects
%doc %{_texmfdistdir}/doc/latex/lt3rawobjects

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
