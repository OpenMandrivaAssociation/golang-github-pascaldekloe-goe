# Run tests in check section
%bcond_without check

# https://github.com/pascaldekloe/goe
%global goipath         github.com/pascaldekloe/goe
%global commit          57f6aae5913c64c9bcae5dbdffd33365b5a7f138

%gometa

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Common enterprise features for the Go programming language
# Detected licences
# - *No copyright* UNKNOWN at 'LICENSE'
License:        CC0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20181113git57f6aae
- First package for Fedora

