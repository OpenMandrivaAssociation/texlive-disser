Name:		texlive-disser
Version:	1.5.0
Release:	1
Summary:	Class and templates for typesetting dissertations in Russian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/disser
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/disser.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/disser.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/disser.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Disser comprises a document class and set of templates for
typesetting dissertations in Russian. One of its primary
advantages is a simplicity of format specification for
titlepage, headers and elements of automatically generated
lists (table of contents, list of figures, etc). Bibliography
styles, that conform to the requirements of the Russian
standard GOST R 7.0.11-2011, are provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/disser
%{_texmfdistdir}/tex/latex/disser
%doc %{_texmfdistdir}/doc/latex/disser
#- source
%doc %{_texmfdistdir}/source/latex/disser

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
