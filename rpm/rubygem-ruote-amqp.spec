#
# spec file for package rubygem-ruote-amqp (Version 2.1.10lbt1)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           rubygem-ruote-amqp
Version:        2.2.0.1
Release:        1
%define mod_name ruote-amqp
#
Group:          Development/Languages/Ruby
License:        GPLv2+ or Ruby
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
BuildRequires:  rubygem-amqp >= 0.7.0
Requires:       rubygem-amqp >= 0.7.0
BuildRequires:  rubygem-amqp < 0.7.1
Requires:       rubygem-amqp < 0.7.1
BuildRequires:  rubygem-ruote >= 2.2.0
Requires:       rubygem-ruote >= 2.2.0
#
Url:            http://github.com/kennethkalmer/ruote-amqp
Source:         %{mod_name}-%{version}.gem
#
Summary:        AMQP participant/listener pair for ruote 2.1
%description
AMQP participant/listener pair for ruote 2.2

%prep
%build
%install
%gem_install %{S:0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%changelog
