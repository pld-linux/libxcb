Summary:	X protocol C-language Binding library
Summary(pl):	XCB - biblioteka dowi±zañ jêzyka C do protoko³u X
Name:		libxcb
Version:	0.9
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	578037c76d791d4623f0f8b3e14fbabc
URL:		http://xcb.freedesktop.org/
BuildRequires:	check >= 0.8.2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 0.9
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol C-language Binding library.

%description -l pl
XCB - biblioteka dowi±zañ jêzyka C do protoko³u X.

%package devel
Summary:	Header files for XCB library
Summary(pl):	Pliki nag³ówkowe biblioteki XCB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libXdmcp-devel
Requires:	xorg-proto-xproto-devel

%description devel
Header files for XCB library.

%description devel -l pl
Pliki nag³ówkowe biblioteki XCB.

%package static
Summary:	Static XCB library
Summary(pl):	Statyczna biblioteka XCB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB library.

%description static -l pl
Statyczna biblioteka XCB.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_libdir}/libXCB*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXCB*.so
%{_libdir}/libXCB*.la
%{_includedir}/X11/XCB/*.h
%{_pkgconfigdir}/xcb*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXCB*.a
