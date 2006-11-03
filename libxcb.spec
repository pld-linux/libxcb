Summary:	X protocol C-language Binding library
Summary(pl):	XCB - biblioteka dowi±zañ jêzyka C do protoko³u X
Name:		libxcb
Version:	0.9.93
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	7967d0d4347502bc9af5373767afc748
URL:		http://xcb.freedesktop.org/
BuildRequires:	check >= 0.8.2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 0.9.93
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol C-language Binding library.

libxcb provides an interface to the X Window System protocol, slated to
replace the current Xlib interface. It has several advantages over
Xlib, including:
- size: small library and lower memory footprint
- latency hiding: batch several requests and wait for the replies later
- direct protocol access: one-to-one mapping between interface and protocol
- proven thread support: transparently access XCB from multiple threads
- easy extension implementation: interfaces auto-generated from XML-XCB

Xlib can also use XCB as a transport layer, allowing software to make
requests and receive responses with both, which eases porting to XCB.
However, client programs, libraries, and toolkits will gain the most
benefit from a native XCB port.

%description -l pl
XCB - biblioteka dowi±zañ jêzyka C do protoko³u X.

libxcb udostêpnia interfejs do protoko³u X Window System, maj±cy
zast±piæ aktualny interfejs Xlib. Ma kilka zalet w stosunku do Xliba,
w tym:
- rozmiar: ma³a biblioteka i niewielki narzut pamiêciowy
- ukrywanie opó¼nieñ: kolejkowanie kilku ¿±dañ i oczekiwanie na
  odpowied¼ pó¼niej
- bezpo¶redni dostêp do protoko³u: odwzorowanie 1-1 miêdzy interfejsem
  a protoko³em
- sprawdzon± obs³ugê w±tków: bezpo¶redni dostêp do XCB z wielu w±tków
- ³atwe implementowanie rozszerzeñ: automatyczne generowanie
  interfejsów z XML-XCB

Xlib mo¿e tak¿e u¿ywaæ XCB jako warstwy transportowej, pozwalaj±c
programom wykonywaæ ¿±dania i odbieraæ odpowiedzi poprzez oba
interfejsy, co u³atwia przechodzenie na XCB. Jednak programy
klienckie, biblioteki i toolkity zyskaj± wiêcej na natywnym porcie
XCB.

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
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libxcb*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb*.so
%{_libdir}/libxcb*.la
%{_includedir}/xcb
%{_pkgconfigdir}/xcb*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb*.a
