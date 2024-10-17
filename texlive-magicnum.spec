Name:		texlive-magicnum
Version:	52983
Release:	2
Summary:	Access TeX systems' "magic numbers"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/magicnum
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magicnum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magicnum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magicnum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows access to the various parameter values in
TeX (catcode values), e-TeX (group, if and node types, and
interaction mode), and LuaTeX (pdfliteral mode) by a
hierarchical name system.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/magicnum
%{_texmfdistdir}/tex/generic/magicnum
%{_texmfdistdir}/scripts/magicnum
%doc %{_texmfdistdir}/doc/latex/magicnum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
