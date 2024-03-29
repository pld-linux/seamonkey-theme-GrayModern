%define		_realname	graymodern
%define		_snap		2007-06-18_sea1.1
Summary:	Theme like Modern, only gray
Summary(pl.UTF-8):	Motyw identyczny jak Modern, tylko że szary
Name:		seamonkey-theme-GrayModern
Version:	2007.06.18
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	7b61f2e7c1ecd7e225d5be44d521634b
Source1:	gen-installed-chrome.sh
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	seamonkey >= 1.1
Requires(post,postun):	textutils
Requires:	seamonkey >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/seamonkey/chrome

%description
Theme for SeaMonkey, like Modern only gray.

%description -l pl.UTF-8
Motyw dla SeaMonkey, identyczny jak Modern, tylko że szary.

%prep
%setup -q -c -T
install %{SOURCE0} %{_realname}.jar
install %{SOURCE1} .
./gen-installed-chrome.sh skin %{_realname}.jar > %{_realname}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	%{_sbindir}/seamonkey-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/seamonkey-chrome+xpcom-generate ] || %{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
