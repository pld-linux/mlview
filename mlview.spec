Summary:	XML Editor for GNOME
Summary(pl):	Edytor XML dla GNOME
Name:		mlview
Version:	0.6.2
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	0cbdd1b55f8ad7aa1769ddac38ffea9d
URL:		http://www.freespiders.org/projects/gmlview/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-mlview (GNOME Markup Language Viewer) is an XML editor for
GNOME. It include support to view, edit, validate and save xml
document by graphically manipulate the xml Document Object Model.

%description -l pl
gnome-mlview (GNOME Markup Language Viewer) to edytor XML dla GNOME.
Umożliwia przeglądanie, modyfikowanie oraz zapisywanie dokumentów XML
z graficznym interfejsem.

%prep
%setup -q

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig

%postun
/sbin/ldconfig
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mlv
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/mlview
%{_desktopdir}/mlview.desktop
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
