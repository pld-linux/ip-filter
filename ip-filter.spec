Summary:	IP Filter
Summary(pl):	Filtr IP
Name:		ip-filter
Version:	3.3.12
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://coombs.anu.edu.au/pub/net/ip-filter/ip-fil%{version}.tar.gz
# Source0-md5:	19461233002ed127d0fbc4a95a673aac
#Patch0:
#BuildRequires:
#Requires:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IP Filter is a TCP/IP packet filter, suitable for use in a firewall
environment. To use, it can either be used as a loadable kernel module
or incorporated into your UNIX kernel; use as a loadable kernel module
where possible is highly recommended. Scripts are provided to install
and patch system files, as required.

%description -l pl
IP Filter to filtr pakietów TCP/IP, przeznaczony do u¿ycia w
¶rodowiskach typu firewall. By móc go u¿ywaæ musi istnieæ wsparcie
przez odpowiedni modu³ ³adowalny lub w³±czone w j±dro; u¿ycie w
postaci modu³u jest bardzo zalecane. Skrypty s± przygotowane do tego
by zainstalowaæ i zmodyfikowaæ odpowiednie pliki systemowe w stopniu w
jakim jest to konieczne.

%prep
%setup -q -n ip_fil%{version}

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
