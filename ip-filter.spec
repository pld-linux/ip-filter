Summary:	IP Filter
Summary(pl):	Filtr IP
Name:		ip-filter
Version:	3.3.12
Release:	1
Copyright:	GPL
Group:		System
Group(pl):	System
Source0:	ftp://coombs.anu.edu.au/pub/net/ip-filter/ip-fil3.3.12.tar.gz
#Patch0:		
#BuildRequires:	
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description
IP Filter is a TCP/IP packet filter, suitable for use in a firewall environment.
To use, it can either be used as a loadable kernel module or incorporated into 
your UNIX kernel; use as a loadable kernel module where possible is highly 
recommended. Scripts are provided to install and patch system files, as 
required.

%description -l pl

# optional package =====================

#%package
#Summary:	
#Summary(pl):	
#Group:		
#Group(pl):	

#%description 


#%description -l pl
# end of optional package ==============

%prep
%setup -q

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

# optional package

#%files
#%defattr(644,root,root,755)
#%doc
#%attr(,,)
#end of optional package

* %{date} PLD Team <pld-list@pld.org.pl>
All below listed persons can be reached on <cvs_login>@pld.org.pl

$Log: ip-filter.spec,v $
Revision 1.1  2000-03-16 08:32:27  cieciwa
- version 3.3.12,
- build rpm.
