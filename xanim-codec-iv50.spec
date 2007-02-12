Summary:	Indeo 5.0 codec for XAnim
Summary(pl.UTF-8):	Kodek Indeo 5.0 dla XAnima
Name:		xanim-codec-iv50
Version:	1.0
Release:	1
License:	non-distributable, for use with xanim exclusively
Group:		X11/Applications/Graphics
# old dlls at http://xanim.polter.net/dlls/
Source1:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv50_1.0_linuxELFx86c6.tgz
# NoSource1-md5:	40a07db3a47a35ddc64838b11ac5ded6
Source2:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv50_1.0_linuxELFalphaC6.tgz
# NoSource2-md5:	b0f36d6bc262bf84e6b1030e16b3f88f
Source3:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv50_1.0_linuxELFppc.tgz
# NoSource3-md5:	86a09609af80772a7fc7394fcaa0de13
NoSource:	1
NoSource:	2
NoSource:	3
URL:		http://xanim.polter.net/
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Intel Indeo 5.0 codec decompression DLL for XAnim.

%description -l pl.UTF-8
Biblioteka do dekompresji kodeka Intel Indeo 5.0 dla XAnima.

%prep
%ifarch %{ix86}
%setup -q -c -T -a1
%endif
%ifarch alpha
%setup -q -c -T -a2
%endif
%ifarch ppc
%setup -q -c -T -a3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_iv50_*.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc iv50.readme
%attr(755,root,root) %{_libdir}/xanim/vid_iv50_*.xa
