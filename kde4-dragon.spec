%define		_state		stable
%define		orgname		dragon
%define		qtver		4.8.1

Summary:	Dragon Player - very simple Phonon-based media player
Summary(pl.UTF-8):	Dragon Player - bardzo prosty odtwarzacz multimediów oparty na Phononie
Name:		kde4-kdemultimedia
Version:	4.9.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	1b89a6d22f687f1bb0781b29787ffdb8
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libmusicbrainz3-devel >= 1:3.0.0
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xine-lib-devel >= 1:1.0
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
Requires:	kde4-kdebase-workspace-solid >= %{version}
Requires:	kde4-kdelibs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dragon Player - very simple Phonon-based media player.

%description -l pl.UTF-8
Dragon Player - bardzo prosty odtwarzacz multimediów oparty na
Phononie.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files dragon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dragon
%attr(755,root,root) %{_libdir}/kde4/dragonpart.so
%{_datadir}/apps/dragonplayer
%{_datadir}/apps/solid/actions/dragonplayer-opendvd.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_datadir}/config/dragonplayerrc
%{_datadir}/kde4/services/ServiceMenus/dragonplayer_play_dvd.desktop
%{_datadir}/kde4/services/dragonplayer_part.desktop
%{_desktopdir}/kde4/dragonplayer.desktop
%{_iconsdir}/*/*/apps/dragonplayer.png
%{_iconsdir}/*/*/actions/player-volume-muted.png
# FIXME: add -svg-icons subpackage like in kdebase-workspace and put the icons there
#%{_iconsdir}/*/scalable/actions/player-volume-muted.svgz
#%{_iconsdir}/hicolor/scalable/apps/dragonplayer.svgz
%lang(en) %{_kdedocdir}/en/dragonplayer
