#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Webmail-Gmail
Summary:	Mail::Webmail::Gmail - An interface to Google's webmail service
Summary(pl.UTF-8):	Mail::Webmail::Gmail - Interfejs do serwisu Google webmail
Name:		perl-Mail-Webmail-Gmail
Version:	1.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	441c0eac1fa6afac777b0404dec79ed2
URL:		http://search.cpan.org/dist/Mail-Webmail-Gmail/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-SSLeay
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Because Gmail is currently in Beta testing, expect this module to
break as they make updates to their interface. I will attempt to keep
this module in line with the changes they make, but, if after updating
to the newest version of this module, the feature that you require
still doesn't work, please contact me with the issue.

%description -l pl.UTF-8
Ponieważ Gmail jest aktualnie w stanie testów beta, ten moduł może
przestać działać w miarę uaktualnień ich interfejsu. Autor będzie
próbował utrzymać ten moduł w synchronizacji ze zmianami, ale, jeśli
po uaktualnieniu do najnowszej wersji modułu, jakaś opcja nadal nie
działa, należy się skontaktować z autorem.

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
%dir %{perl_vendorlib}/Mail/Webmail
%{perl_vendorlib}/Mail/Webmail/*.pm
%{_mandir}/man3/*
