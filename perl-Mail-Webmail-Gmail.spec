#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Webmail-Gmail
Summary:	Mail::Webmail::Gmail - An interface to Google's webmail service
Summary(pl):	Mail::Webmail::Gmail - Interfejs do serwisu Google webmail
Name:		perl-Mail-Webmail-Gmail
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	18e594f8e778f4389ec1362048cfe2b8
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

%description -l pl
Poniewa¿ Gmail jest aktualnie w stanie testów beta, ten modu³ mo¿e
przestaæ dzia³aæ w miarê uaktualnieñ ich interfejsu. Autor bêdzie
próbowa³ utrzymaæ ten modu³ w synchronizacji ze zmianami, ale, je¶li
po uaktualnieniu do najnowszej wersji modu³u, jaka¶ opcja nadal nie
dzia³a, nale¿y siê skontaktowaæ z autorem.

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
%{perl_vendorlib}/Mail/Webmail/*.pm
%{_mandir}/man3/*
