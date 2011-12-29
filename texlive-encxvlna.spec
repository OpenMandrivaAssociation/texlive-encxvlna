# revision 15878
# category Package
# catalog-ctan /macros/generic/encxvlna
# catalog-date 2008-08-19 08:58:40 +0200
# catalog-license lppl
# catalog-version undef
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools for inserting nonbreakable spaces
after nonsyllabic prepositions and single letter conjunctions
as required by Czech and Slovak typographical rules. It is
implemented using encTeX and provides files both for plain TeX
and LaTeX. The LaTeX solution tries to avoid conflicts with
other packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
