%define		_realname	graymodern
%define		_snap		2006-01-31_sea1.0
Summary:	Theme like Modern, only gray
Summary(pl):	Motyw identyczny jak Modern, tylko ¿e szary
Name:		seamonkey-theme-GrayModern
Version:	2006.01.31
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	b4beb450cc1577cec3b2f6dce01be5c5
Source1:	gen-installed-chrome.sh
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	seamonkey >= 1.0
Requires(post,postun):	textutils
Requires:	seamonkey >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/seamonkey/chrome

%description
Theme for SeaMonkey, like Modern only gray.

%description -l pl
Motyw dla SeaMonkey, identyczny jak Modern, tylko ¿e szary.

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
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
