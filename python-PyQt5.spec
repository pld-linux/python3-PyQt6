%define		module	PyQt5
# minimal required sip version
%define		sip_ver	2:4.16
# last qt version covered by these bindings (minimal required is currently 4.1.0)
%define		qt_ver	%{version}

Summary:	Python bindings for the Qt4 toolkit
Summary(pl.UTF-8):	Dowiązania do toolkitu Qt4 dla Pythona
Name:		python-%{module}
Version:	5.3.2
Release:	1
License:	GPL v2 or GPL v3 with FLOSS exception
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyqt/PyQt-gpl-%{version}.tar.gz
# Source0-md5:	81ef608fa4f3961918106d0ca07aa68a
URL:		http://www.riverbankcomputing.com/software/pyqt/
# most of BR comes from configure.py
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	phonon-devel
BuildRequires:	pkgconfig
BuildRequires:	python-dbus-devel >= 0.80
BuildRequires:	python-sip-devel >= %{sip_ver}
BuildRequires:	qt5-build >= 4.3.3-3
BuildRequires:	qt5-qmake >= 4.3.3-3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-libs
Requires:	python-dbus >= 0.80
Requires:	python-sip >= %{sip_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt5 is a set of Python bindings for the Qt5 toolkit. The bindings
are implemented as a set of Python modules: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns and phonon.

%description -l pl.UTF-8
PyQt5 to zbiór dowiązań do Qt5 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: QtCore, QtDeclarative,
QtDesigner, QtGui, QtHelp, QtMultimedia, QtNetwork, QtOpenGL,
QtScript, QtScriptTools, QtSql, QtSvg, QtTest, QtWebKit, QtXml,
QtXmlPatterns oraz phonon.

%package devel
Summary:	Files needed to build other bindings based on Qt5
Summary(pl.UTF-8):	Pliki potrzebne do budowania innych dowiązań opartych na Qt5
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-sip-devel

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt5 classes (e.g. KDE or your own).

%description devel -l pl.UTF-8
Pliki potrzebne do budowania innych dowiązań do klas C++
dziedziczących z dowolnej klasy Qt5 (np. KDE lub własnych).

%package devel-tools
Summary:	PyQt5 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyQt5
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel-tools
PyQt5 development tools: pylupdate5, pyrcc5, pyuic5.

%description devel-tools -l pl.UTF-8
Narzędzia programistyczne PyQt5: pylupdate5, pyrcc5, pyuic5.

%package examples
Summary:	Examples for PyQt5
Summary(pl.UTF-8):	Przykłady do PyQt5
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt5.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt5.

%package -n qscintilla2-%{module}-api
Summary:	PyQt5 API file for QScintilla
Summary(pl.UTF-8):	Plik API PyQt5 dla QScintilli
Group:		Libraries/Python
Requires:	python-qscintilla2 >= 2.2-2

%description -n qscintilla2-%{module}-api
PyQt4 API file can be used by the QScintilla editor component to
enable the use of auto-completion and call tips when editing PyQt5
code.

%description -n qscintilla2-%{module}-api -l pl.UTF-8
Plik API PyQt4 może być używany przez komponent edytora QScintilla aby
umożliwić automatyczne dopełnianie i podpowiedzi przy modyfikowaniu
kodu wykorzystującego PyQt5.

%prep
%setup -q -n PyQt-gpl-%{version}
%{__sed} -i 's,pyuic.py,pyuic.pyc,' configure.py
# small hack to build for shared libs - symbol QT_SHARED not defined anymore?
%{__sed} -i 's/qt_shared = lines\[.*\]/qt_shared = "y"/' configure.py
%{__sed} -i 's/resp = sys.stdin.readline.*/resp = "yes"/' configure.py

%build
%{__python} configure.py \
	--confirm-license \
	-c -j 3 \
	-a \
	-b %{_bindir} \
	-d %{py_sitedir} \
	-q "%{_bindir}/qmake-qt5" \
	-v %{_sipfilesdir}/%{module} \
	LIBDIR_QT="%{_libdir}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

# don't use py_postclean, leave *.py in %{py_sitedir}/PyQt4/uic/widget-plugins
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt5/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt5/uic/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt5/uic/Compiler/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt5/uic/Loader/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt5/uic/port_v2/*.py
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyQt5/uic/port_v3/*.py

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libpyqt5.so
%dir %{py_sitedir}/PyQt5
%attr(755,root,root) %{py_sitedir}/PyQt5/Qt.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtCore.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtDBus.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtDesigner.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtGui.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtHelp.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtNetwork.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtOpenGL.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtSql.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtTest.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtWidgets.so
%attr(755,root,root) %{py_sitedir}/PyQt5/_QOpenGLFunctions_2_0.so
%{py_sitedir}/PyQt5/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/dbus/mainloop/pyqt5.so

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt5

%files devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pylupdate5
%attr(755,root,root) %{_bindir}/pyrcc5
%attr(755,root,root) %{_bindir}/pyuic5
%{py_sitedir}/PyQt5/uic

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n qscintilla2-%{module}-api
%defattr(644,root,root,755)
%{_datadir}/qt5/qsci/api/python/PyQt5.api
