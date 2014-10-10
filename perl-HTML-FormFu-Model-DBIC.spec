%define upstream_name    HTML-FormFu-Model-DBIC
%define upstream_version 0.09002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Integrate HTML::FormFu with DBIx::Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(Class::Factory::Util)
BuildRequires:	perl(DateTime::Format::SQLite)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::FormFu)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Moose::Meta::Attribute::Custom::Trait::Chained)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(boolean)

BuildArch:	noarch

%description
Integrate HTML::FormFu with DBIx::Class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.20-1mdv2011
+ Revision: 690529
- update to new version 0.09002

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 662070
- update to new version 0.09000

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.80.20-2
+ Revision: 654343
- rebuild for updated spec-helper

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.20-1mdv2011.0
+ Revision: 628772
- new version

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 477625
- update to 0.06000

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.30-1mdv2010.1
+ Revision: 471530
- adding missing buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- import perl-HTML-FormFu-Model-DBIC


* Sun Nov 29 2009 cpan2dist 0.05003-1mdv
- initial mdv release, generated with cpan2dist
