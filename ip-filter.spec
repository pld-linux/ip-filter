Summary:	IP Filter
Summary(pl):	Filtr IP
Name:		ip-filter
Version:	3.3.12
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://coombs.anu.edu.au/pub/net/ip-filter/ip-fil%{version}.tar.gz
#Patch0:	
#BuildRequires:	
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
IP Filter is a TCP/IP packet filter, suitable for use in a firewall
environment. To use, it can either be used as a loadable kernel module
or incorporated into your UNIX kernel; use as a loadable kernel module
where possible is highly recommended. Scripts are provided to install
and patch system files, as required.

%description -l pl

%prep
%setup -q -n ip_fil%{version}

#%patch

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
