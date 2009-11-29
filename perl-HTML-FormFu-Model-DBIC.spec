%define upstream_name    HTML-FormFu-Model-DBIC
%define upstream_version 0.05003

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Integrate HTML::FormFu with DBIx::Class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(DateTime::Format::SQLite)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::FormFu)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Task::Weaken)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


