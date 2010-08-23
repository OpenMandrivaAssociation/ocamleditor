Name:           ocamleditor
Version:        1.4.2
Release:        %mkrel 1
Summary:        Source code editor and build tool for OCaml
License:        GPL
Group:          Development/Other
URL:            http://ocamleditor.forge.ocamlcore.org/
Source0:        http://forge.ocamlcore.org/frs/download.php/437/OCamlEditor-%{version}test.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  ocamldsort
BuildRequires:  ocaml-sources
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  ocaml-xml-light-devel
Requires:  ocaml-lablgtk2
Requires:  ocaml-xml-light

%description
Features:
* Customizable syntax highlighting
* Automatic indentation to match preceding line
* Commenting/uncommenting of code blocks
* Highlighting of matching delimiters
* Completion popup with types description
* Tabbed views
* Switch between interface and implementation
  with automatic interface generation
* Automatic detection of dependencies
* External build tasks
* ...

%prep
%setup -q -n OCamlEditor-%{version}
cp -R /usr/src/ocaml src/ocaml-src

%build
pushd src
pushd ocaml-src
./configure
make world world.opt
popd
ocaml build.ml
popd

%install
rm -rf %{buildroot}
export PREFIX="%{buildroot}/usr"
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
pushd src
ocaml build.ml install
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE CHANGES
%{_bindir}/ocamleditor
%{_bindir}/oebuild
%{_bindir}/oebuild.opt
%{_datadir}/pixmaps/
