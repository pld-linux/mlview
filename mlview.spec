Summary:	XML Editor for GNOME
Summary(pl):	Edytor XML dla GNOME
Name:		mlview
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://freesoftware.fsf.org/download/mlview/tarballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-aclocal.patch
URL:		http://www.freesoftware.fsf.org/mlview/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.18 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gnome-mlview (Gnome Markup Language Viewer) is an XML editor for
GNOME. It include support to view, edit, validate and save xml
document by graphically manipulate the xml Document Object Model.

%description -l pl
gnome-mlview (Gnome Markup Language Viewer) to edytor XML dla GNOME.
Umo¿liwia przegl±danie, modyfikowanie oraz zapisywanie dokumentów XML
z graficznym interfejsem.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# Install an entry in the GNOME Applications menu:
install -d $RPM_BUILD_ROOT%{_applnkdir}/Applications
cat >$RPM_BUILD_ROOT%{_applnkdir}/Applications/mlview.desktop <<EOF
[Desktop Entry]
Name=MlView
Comment=MlView - XML editor for GNOME
Comment[fr]=MlView - Éditeur XML pour GNOME
Comment[pl]=MlView - edytor XML dla GNOME
Exec=mlv
Terminal=0
Type=Application
EOF

# there is fr file but is not correctly installed, due to generally broken AM support /klakier
#%find_lang %{name} --with-gnome

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mlv
%attr(755,root,root) %{_bindir}/mlview
%attr(755,root,root) %{_bindir}/gnome-mlview
%attr(755,root,root) %{_bindir}/gmlview
%{_applnkdir}/Applications/mlview.desktop
%{_datadir}/gnome-mlview
