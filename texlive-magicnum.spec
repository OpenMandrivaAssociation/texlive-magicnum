%global tl_name magicnum
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Access TeX systems magic numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/magicnum
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/magicnum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/magicnum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/magicnum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows access to the various parameter values in TeX
(catcode values), e-TeX (group, if and node types, and interaction
mode), and LuaTeX (pdfliteral mode) by a hierarchical name system.

