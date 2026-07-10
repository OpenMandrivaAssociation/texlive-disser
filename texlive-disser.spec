%global tl_name disser
%global tl_revision 43417

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.0
Release:	%{tl_revision}.1
Summary:	Class and templates for typesetting dissertations in Russian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/disser
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/disser.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/disser.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/disser.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Disser comprises a document class and set of templates for typesetting
dissertations in Russian. One of its primary advantages is a simplicity
of format specification for titlepage, headers and elements of
automatically generated lists (table of contents, list of figures, etc).
Bibliography styles, that conform to the requirements of the Russian
standard GOST R 7.0.11-2011, are provided.

