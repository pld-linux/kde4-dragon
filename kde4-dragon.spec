%define		_state		stable
%define		orgname		dragon
%define		qtver		4.8.1

Summary:	Dragon Player - very simple Phonon-based media player
Summary(pl.UTF-8):	Dragon Player - bardzo prosty odtwarzacz multimediów oparty na Phononie
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	3029633dc44dca9b4b679eed2368c1f2
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdebase-workspace-solid >= 4.11.4
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kde4-kdemultimedia-dragon < 4.8.99-1
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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dragon
%attr(755,root,root) %{_libdir}/kde4/dragonpart.so
%{_datadir}/apps/dragonplayer
%{_datadir}/apps/solid/actions/dragonplayer-opendvd.desktop
%{_datadir}/config/dragonplayerrc
%{_datadir}/kde4/services/ServiceMenus/dragonplayer_play_dvd.desktop
%{_datadir}/kde4/services/dragonplayer_part.desktop
%{_desktopdir}/kde4/dragonplayer.desktop
%{_iconsdir}/*/*/apps/dragonplayer.*
%{_iconsdir}/*/*/actions/player-volume-muted.png
# FIXME: add -oxygen-svg-icons subpackage like in kdebase-workspace and put the icons there
#%{_iconsdir}/oxygen/scalable/actions/player-volume-muted.svgz
%lang(en) %{_kdedocdir}/en/dragonplayer
%{_mandir}/man1/dragon.1*
