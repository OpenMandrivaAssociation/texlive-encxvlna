Name:		texlive-encxvlna
Version:	20080819
Release:	1
Summary:	Insert nonbreakable spaces, using encTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/encxvlna
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/encxvlna.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/encxvlna.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides tools for inserting nonbreakable spaces
after nonsyllabic prepositions and single letter conjunctions
as required by Czech and Slovak typographical rules. It is
implemented using encTeX and provides files both for plain TeX
and LaTeX. The LaTeX solution tries to avoid conflicts with
other packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/encxvlna/encxvlna.sty
%{_texmfdistdir}/tex/plain/encxvlna/encxvlna.tex
%doc %{_texmfdistdir}/doc/generic/encxvlna/License.txt
%doc %{_texmfdistdir}/doc/generic/encxvlna/README
%doc %{_texmfdistdir}/doc/generic/encxvlna/encxvlna.pdf
%doc %{_texmfdistdir}/doc/generic/encxvlna/encxvlna.tex
%doc %{_texmfdistdir}/doc/generic/encxvlna/vlna-inc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}