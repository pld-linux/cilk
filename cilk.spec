#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	Cilk compiler
Summary(pl):	Kompilator Cilka
Name:		cilk
Version:	5.4.2.2
%define	_rev	1708
Release:	0.1
License:	GPL v2 and LGPL
Group:		Development/Languages
Source0:	http://bradley.csail.mit.edu/~bradley/cilk/downloads/%{name}-%{version}_%{_rev}.tar.bz2
# Source0-md5:	1046f684ac72076106574fcc8326e612
URL:		http://supertech.lcs.mit.edu/cilk/
Patch0:		%{name}-update.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cilk is a language for multithreaded parallel programming based on
ANSI C. Cilk is designed for general-purpose parallel programming, but
it is especially effective for exploiting dynamic, highly asynchronous
parallelism, which can be difficult to write in data-parallel or
message-passing style.

#%%description -l pl
#TODO

%package static
Summary:	Static cilk libraries
Summary(pl):	Statyczne biblioteki cilka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static cilk libraries.

%description static -l pl
Statyczne biblioteki cilka.

%prep
%setup -q -n %{version}
%patch0 -p1
%{!?with_tests:sed 's/ examples / /' -i Makefile.in}

%build
%{__libtoolize}
%{__aclocal} -I m4dir
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
# contains libcilkrt0*.a
%{_libdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
