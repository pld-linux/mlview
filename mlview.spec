Summary:	XML Editor for GNOME
Summary(pl):	Edytor XML-a dla GNOME
Name:		mlview
Version:	0.6.3
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	6975d10f92deddfee4b02153aafc6bcd
Patch0:		%{name}-locale-names.patch
URL:		http://www.freespiders.org/projects/gmlview/
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnome-devel >= 2.2
BuildRequires:	eel-devel >= 2.2
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libxslt >= 1.0.33
BuildRequires:	libxml2-devel >= 2.4.18
BuildRequires:	gtk+2-devel >= 2.2
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-mlview (GNOME Markup Language Viewer) is an XML editor for
GNOME. It include support to view, edit, validate and save xml
document by graphically manipulate the xml Document Object Model.

%description -l pl
gnome-mlview (GNOME Markup Language Viewer) to edytor XML-a dla GNOME.
Umo¿liwia przegl±danie, modyfikowanie oraz zapisywanie dokumentów XML
z graficznym interfejsem.

%prep
%setup -q
%patch0 -p1                                                                     
                                                                                
mv po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove useless static file
rm -f $RPM_BUILD_ROOT%{_libdir}/libmlview.la

%find_lang %{name} --with-gnome

%clean
rm -fr $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mlv
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/mlview
%{_desktopdir}/mlview.desktop
#%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
