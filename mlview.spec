
%define	_rcver		rc2

Summary:	XML Editor for GNOME
Summary(pl):	Edytor XML dla GNOME
Name:		mlview
Version:	0.0.3
Release:	0.%{_rcver}.1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://freesoftware.fsf.org/download/mlview/tarballs/%{name}-%{version}%{_rcver}.tar.gz
# Source0-md5:	7785e633e4d336c4aa736fa5b2da8528
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-aclocal.patch
URL:		http://www.freesoftware.fsf.org/mlview/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
gnome-mlview (Gnome Markup Language Viewer) is an XML editor for
GNOME. It include support to view, edit, validate and save xml
document by graphically manipulate the xml Document Object Model.

%description -l pl
gnome-mlview (Gnome Markup Language Viewer) to edytor XML dla GNOME.
Umo¿liwia przegl±danie, modyfikowanie oraz zapisywanie dokumentów XML
z graficznym interfejsem.

%prep
%setup -q -n %{name}-%{version}%{_rcver}
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Editors/XML,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Editors/XML
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mlv
%attr(755,root,root) %{_bindir}/mlview
%attr(755,root,root) %{_bindir}/gnome-mlview
%attr(755,root,root) %{_bindir}/gmlview
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/gnome-mlview
%{_applnkdir}/Editors/XML/mlview.desktop
%{_pixmapsdir}/*
