Name:		texlive-encxvlna
Version:	34087
Release:	1
Summary:	Insert nonbreakable spaces, using encTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/encxvlna
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/encxvlna.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/encxvlna.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
