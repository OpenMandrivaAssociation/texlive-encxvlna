%global tl_name encxvlna
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Insert nonbreakable spaces, using encTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/encxvlna
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/encxvlna.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/encxvlna.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools for inserting nonbreakable spaces after
nonsyllabic prepositions and single letter conjunctions as required by
Czech and Slovak typographical rules. It is implemented using encTeX and
provides files both for plain TeX and LaTeX. The LaTeX solution tries to
avoid conflicts with other packages.

