# revision 24029
# category Package
# catalog-ctan /macros/latex/contrib/disser
# catalog-date 2011-09-19 19:20:18 +0200
# catalog-license lppl
# catalog-version 1.1.8
Name:		texlive-disser
Version:	1.1.8
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Disser comprises a document class and set of templates for
typesetting dissertations in Russian. One of its primary
advantages is a simplicity of format specification for
titlepage, headers and elements of automatically generated
lists (table of contents, list of figures, etc). Bibliography
styles, that conform to the requirements of the Russian
standard GOST R 7.0.5-2008, are provided.

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
%{_texmfdistdir}/bibtex/bst/disser/gost705.bst
%{_texmfdistdir}/bibtex/bst/disser/gost705s.bst
%{_texmfdistdir}/bibtex/csf/disser/cp1251lc.csf
%{_texmfdistdir}/makeindex/disser/dtx.ist
%{_texmfdistdir}/tex/latex/disser/autoref.rtx
%{_texmfdistdir}/tex/latex/disser/bachelor.rtx
%{_texmfdistdir}/tex/latex/disser/candidate.rtx
%{_texmfdistdir}/tex/latex/disser/disser.cls
%{_texmfdistdir}/tex/latex/disser/doctor.rtx
%{_texmfdistdir}/tex/latex/disser/gost732.cls
%{_texmfdistdir}/tex/latex/disser/master.rtx
%{_texmfdistdir}/tex/latex/disser/specialist.rtx
%{_texmfdistdir}/tex/latex/disser/titledefs.rtx
%doc %{_texmfdistdir}/doc/latex/disser/ChangeLog
%doc %{_texmfdistdir}/doc/latex/disser/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/README
%doc %{_texmfdistdir}/doc/latex/disser/README.ru
%doc %{_texmfdistdir}/doc/latex/disser/cp1251.csf
%doc %{_texmfdistdir}/doc/latex/disser/include/latex.fig.mk
%doc %{_texmfdistdir}/doc/latex/disser/include/latex.fig.nmk.cmd
%doc %{_texmfdistdir}/doc/latex/disser/include/latex.mk
%doc %{_texmfdistdir}/doc/latex/disser/include/latex.nmk.cmd
%doc %{_texmfdistdir}/doc/latex/disser/manual.tex
%doc %{_texmfdistdir}/doc/latex/disser/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/1.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/app-a.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/concl.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/fig/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/fig/fig.eps
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/fig/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/intro.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/thesis.bib
%doc %{_texmfdistdir}/doc/latex/disser/templates/bachelor/thesis.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/1.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/app-a.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/autoref.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/common.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/concl.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/facsimile.eps
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/sec-facsimile.eps
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/intro.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/review.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/thesis.bib
%doc %{_texmfdistdir}/doc/latex/disser/templates/candidate/thesis.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/1.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/app-a.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/autoref.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/common.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/concl.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/facsimile.eps
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/sec-facsimile.eps
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/intro.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/review.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/thesis.bib
%doc %{_texmfdistdir}/doc/latex/disser/templates/doctor/thesis.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/1.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/app-a.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/concl.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/fig/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/fig/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/intro.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/thesis.bib
%doc %{_texmfdistdir}/doc/latex/disser/templates/master/thesis.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/1.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/app-a.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/concl.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/fig/Makefile
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/fig/fig.eps
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/fig/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/intro.tex
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/nomake.cmd
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/thesis.bib
%doc %{_texmfdistdir}/doc/latex/disser/templates/specialist/thesis.tex
#- source
%doc %{_texmfdistdir}/source/latex/disser/autoref.dtx
%doc %{_texmfdistdir}/source/latex/disser/bachelor.dtx
%doc %{_texmfdistdir}/source/latex/disser/candidate.dtx
%doc %{_texmfdistdir}/source/latex/disser/chapter.dtx
%doc %{_texmfdistdir}/source/latex/disser/counters.dtx
%doc %{_texmfdistdir}/source/latex/disser/custom.dtx
%doc %{_texmfdistdir}/source/latex/disser/disser.dtx
%doc %{_texmfdistdir}/source/latex/disser/disser.ins
%doc %{_texmfdistdir}/source/latex/disser/doctor.dtx
%doc %{_texmfdistdir}/source/latex/disser/env.dtx
%doc %{_texmfdistdir}/source/latex/disser/floats.dtx
%doc %{_texmfdistdir}/source/latex/disser/footnote.dtx
%doc %{_texmfdistdir}/source/latex/disser/gost705.dtx
%doc %{_texmfdistdir}/source/latex/disser/gost732.dtx
%doc %{_texmfdistdir}/source/latex/disser/lists.dtx
%doc %{_texmfdistdir}/source/latex/disser/master.dtx
%doc %{_texmfdistdir}/source/latex/disser/page.dtx
%doc %{_texmfdistdir}/source/latex/disser/part.dtx
%doc %{_texmfdistdir}/source/latex/disser/sections.dtx
%doc %{_texmfdistdir}/source/latex/disser/specialist.dtx
%doc %{_texmfdistdir}/source/latex/disser/titledefs.dtx
%doc %{_texmfdistdir}/source/latex/disser/titlepage.dtx
%doc %{_texmfdistdir}/source/latex/disser/toc.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
