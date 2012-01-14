#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Crontab
Summary:	Set::Crontab - expand crontab(5)-style integer lists
Summary(pl.UTF-8):	Set::Crontab - rozszerzanie list liczb w notacji crontab(5)
Name:		perl-Set-Crontab
Version:	1.03
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Set/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c900a24a789203f4beebf91f5752e984
URL:		http://search.cpan.org/dist/Set-Crontab/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Crontab parses crontab-style lists of integers and defines some
utility functions to make it easier to deal with them.

%description -l pl.UTF-8
Set::Crontab przetwarza listy liczb całkowitych w notacji crontaba i
definiuje kilka użytecznych funkcji ułatwiających obsługę ich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Set/Crontab.pm
%{_mandir}/man3/*
