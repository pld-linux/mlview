Summary:	XML Editor for GNOME
Name:		mlview
Version:	0.0.1.9
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://freesoftware.fsf.org/download/mlview/tarballs/%{name}-%{version}.tar.gz
URL:		http://www.freesoftware.fsf.org/mlview/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	libxml2 >= 2.4.18 
Requires:	gnome-libs >= 1.2.11

%description
gnome-mlview (Gnome Markup language Viewer) is an XML editor for
GNOME. It include support to view, edit, validate and save xml
document by graphically manipulate the xml Document Object Model.

%prep
%setup -q

%build
#aclocal
#automake
#autoconf
%configure2_13
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
