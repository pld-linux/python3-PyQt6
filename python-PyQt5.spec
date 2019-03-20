# TODO:
# - __pycache__ for python3-PyQt5-uic
# - Fix  /usr/local/lib64/python3.6/site-packages/PyQt5/*.pyi files.
#
# Conditional build:
%bcond_without	python2	# CPython 2.x modules
%bcond_without	python3	# CPython 3.x modules
%bcond_without	webkit		# QT5WebKit support

%ifarch x32
%undefine	with_webkit
%endif

%define		module	PyQt5
# minimal required sip version
%define		sip_ver	2:4.19.14-1
# last qt version covered by these bindings (minimal required is currently 5.0.0)
# %define		qt_ver	%{version}
%define		qt_ver	5.12.0

Summary:	Python 2 bindings for the Qt5 toolkit
Summary(pl.UTF-8):	Wiązania Pythona 2 do toolkitu Qt5
Name:		python-%{module}
Version:	5.12.1
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	https://www.riverbankcomputing.com/static/Downloads/PyQt5/PyQt5_gpl-%{version}.tar.gz
# Source0-md5:	67508b652098d2e05c4c2b5baeb170cc
Patch0:		install.patch
URL:		http://www.riverbankcomputing.com/software/pyqt/
# most of BR comes from configure.py
BuildRequires:	Qt5Bluetooth-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Designer-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Help-devel >= %{qt_ver}
BuildRequires:	Qt5Location-devel >= %{qt_ver}
BuildRequires:	Qt5Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt5MultimediaWidgets-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Nfc-devel >= %{qt_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt_ver}
BuildRequires:	Qt5Positioning-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sensors-devel >= %{qt_ver}
BuildRequires:	Qt5SerialPort-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5UiTools-devel >= %{qt_ver}
BuildRequires:	Qt5WebChannel-devel >= %{qt_ver}
%{?with_webkit:BuildRequires:	Qt5WebKit-devel >= %{qt_ver}}
BuildRequires:	Qt5WebSockets-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	Qt5XmlPatterns-devel >= %{qt_ver}
BuildRequires:	dbus-devel >= 1
BuildRequires:	pkgconfig
# configure.py does: "from PyQt5 import sip" but sip doesn't provide PyQt5/__init__.py file,
# and thus sip cannot be import. That's why we require python-PyQt5 (which provides __init__.py)
# here. Only for python2 since python3 can import from directory without __init__.py file.
%{?with_python2:BuildRequires:  python-PyQt5 >= 5.11.2}
BuildRequires:	python-dbus-devel >= 0.80
BuildRequires:	python-PyQt5-sip >= %{sip_ver}
BuildRequires:	python-sip-devel >= %{sip_ver}
BuildRequires:	python3-dbus >= 0.80
BuildRequires:	python3-PyQt5-sip >= %{sip_ver}
BuildRequires:	python3-sip-devel >= %{sip_ver}
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-dbus >= 0.80
Requires:	python-libs
Requires:	python-PyQt5-sip >= %{sip_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt5 is a set of Python bindings for the Qt5 toolkit. The bindings
are implemented as a set of Python modules: Qt, QtBluetooth, QtCore,
QtDBus, QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras and QtXmlPatterns.

This package contains Python 2 modules.

%description -l pl.UTF-8
PyQt5 to zbiór dowiązań do Qt5 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: Qt, QtBluetooth, QtCore, QtDBus,
QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras oraz QtXmlPatterns.

Ten pakiet zawiera moduły Pythona 2.

%package uic
Summary:	pyuic5 development tool for Python 2
Summary(pl.UTF-8):	Narzędzie programistyczne pyuic5 dla Pythona 2
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description uic
pyuic5 development tool for Python 2.

%description uic -l pl.UTF-8
Narzędzie programistyczne pyuic5 dla Pythona 2.

%package -n python3-PyQt5
Summary:	Python 3 bindings for the Qt5 toolkit
Summary(pl.UTF-8):	Wiązania Pythona 3 do toolkitu Qt5
Group:		Libraries/Python
Requires:	python3-dbus >= 0.80
Requires:	python3-libs
Requires:	python3-PyQt5-sip >= %{sip_ver}

%description -n python3-PyQt5
PyQt5 is a set of Python bindings for the Qt5 toolkit. The bindings
are implemented as a set of Python modules: Qt, QtBluetooth, QtCore,
QtDBus, QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras and QtXmlPatterns.

This package contains Python 3 modules.

%description -n python3-PyQt5 -l pl.UTF-8
PyQt5 to zbiór dowiązań do Qt5 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: Qt, QtBluetooth, QtCore, QtDBus,
QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras oraz QtXmlPatterns.

Ten pakiet zawiera moduły Pythona 3.

%package -n python3-PyQt5-uic
Summary:	pyuic5 development tool for Python 3
Summary(pl.UTF-8):	Narzędzie programistyczne pyuic5 dla Pythona 3
Group:		Development/Tools
Requires:	python3-PyQt5 = %{version}-%{release}

%description -n python3-PyQt5-uic
pyuic5 development tool for Python 3.

%description -n python3-PyQt5-uic -l pl.UTF-8
Narzędzie programistyczne pyuic5 dla Pythona 3.

%package devel-tools
Summary:	PyQt5 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyQt5
Group:		Development/Tools
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Xml >= %{qt_ver}
%if %{with python2}
Requires:	%{name} = %{version}-%{release}
%else
Requires:	python3-PyQt5 = %{version}-%{release}
%endif

%description devel-tools
PyQt5 development tools: pylupdate5, pyrcc5.

Note: this package doesn't depend on Python version.

%description devel-tools -l pl.UTF-8
Narzędzia programistyczne PyQt5: pylupdate5, pyrcc5.

Uwaga: ten pakiet nie jest zależny od wersji Pythona.

%package examples
Summary:	Examples for PyQt5
Summary(pl.UTF-8):	Przykłady do PyQt5
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt5.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt5.

%package -n sip-PyQt5
Summary:	SIP files needed to build other bindings based on Qt5
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania innych wiązań opartych na Qt5
Group:		Development/Languages/Python
Requires:	sip >= %{sip_ver}
Obsoletes:	python-PyQt5-devel < 5.3.2-4

%description -n sip-PyQt5
SIP files needed to build other bindings for C++ classes that inherit
from any of the Qt5 classes (e.g. KDE or your own).

%description -n sip-PyQt5 -l pl.UTF-8
Pliki SIP potrzebne do budowania innych wiązań do klas C++
dziedziczących z dowolnej klasy Qt5 (np. KDE lub własnych).

%package -n Qt5Designer-plugin-pyqt5
Summary:	Qt5 Designer plugin for Python plugins with widgets
Summary(pl.UTF-8):	Wtyczka Qt5 Designera dla wtyczek Pythona zawierających widgety
# can build only for one python version
%if %{with python2}
Requires:	%{name} = %{version}-%{release}
%else
Requires:	python3-PyQt5 = %{version}-%{release}
%endif

%description -n Qt5Designer-plugin-pyqt5
This is the Qt5 Designer plugin that collects all the Python plugins
it can find as a widget collection to Designer.

%description -n Qt5Designer-plugin-pyqt5 -l pl.UTF-8
Ten pakiet zawiera wtyczkę Qt5 Designera zbierającą wszystkie wtyczki
Pythona, które jest w stanie znaleźć, jako zestaw widgetów dla
Designera.

%package -n qscintilla2-%{module}-api
Summary:	PyQt5 API file for QScintilla
Summary(pl.UTF-8):	Plik API PyQt5 dla QScintilli
Group:		Libraries/Python
Requires:	qscintilla2-qt5 >= 2.2-2

%description -n qscintilla2-%{module}-api
PyQt5 API file can be used by the QScintilla editor component to
enable the use of auto-completion and call tips when editing PyQt5
code.

%description -n qscintilla2-%{module}-api -l pl.UTF-8
Plik API PyQt5 może być używany przez komponent edytora QScintilla aby
umożliwić automatyczne dopełnianie i podpowiedzi przy modyfikowaniu
kodu wykorzystującego PyQt5.

%prep
%setup -q -n PyQt5_gpl-%{version}
%patch0 -p1

%build
%if %{with python2}
install -d build-py2
cd build-py2
%{__python} ../configure.py \
	--no-dist-info \
	--verbose \
	--assume-shared \
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
cd ..
%endif

%if %{with python3}
install -d build-py3
cd build-py3
%{__python3} ../configure.py \
	--no-dist-info \
	--verbose \
	--assume-shared \
	--confirm-license \
	-c -j 3 \
	-a \
	-b %{_bindir} \
	-d %{py3_sitedir} \
	-q "%{_bindir}/qmake-qt5" \
	-v %{_sipfilesdir}/%{module} \
	LIBDIR_QT="%{_libdir}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with python3}
%{__make} -C build-py3 install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyuic5{,-3}
%endif

%if %{with python2}
%{__make} -C build-py2 install \
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
%endif

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README
%dir %{_libdir}/qt5/plugins/PyQt5
%attr(755,root,root) %{_libdir}/qt5/plugins/PyQt5/libpyqt5qmlplugin.so
%dir %{py_sitedir}/PyQt5
%attr(755,root,root) %{py_sitedir}/PyQt5/pylupdate.so
%attr(755,root,root) %{py_sitedir}/PyQt5/pyrcc.so
%attr(755,root,root) %{py_sitedir}/PyQt5/Qt.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtBluetooth.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtCore.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtDBus.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtDesigner.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtGui.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtHelp.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtLocation.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtMultimedia.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtMultimediaWidgets.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtNetwork.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtNfc.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtOpenGL.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtPositioning.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtPrintSupport.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtQml.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtQuick.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtQuickWidgets.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtSensors.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtSerialPort.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtSql.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtSvg.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtTest.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtWebChannel.so
%if %{with webkit}
%attr(755,root,root) %{py_sitedir}/PyQt5/QtWebKit.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtWebKitWidgets.so
%endif
%attr(755,root,root) %{py_sitedir}/PyQt5/QtWebSockets.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtWidgets.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtX11Extras.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtXml.so
%attr(755,root,root) %{py_sitedir}/PyQt5/QtXmlPatterns.so
%attr(755,root,root) %{py_sitedir}/PyQt5/_QOpenGLFunctions_2_0.so
%attr(755,root,root) %{py_sitedir}/PyQt5/_QOpenGLFunctions_2_1.so
%attr(755,root,root) %{py_sitedir}/PyQt5/_QOpenGLFunctions_4_1_Core.so
%{py_sitedir}/PyQt5/__init__.py[co]
%{py_sitedir}/PyQt5/pyrcc_main.py[co]
%{py_sitedir}/PyQt5/pylupdate_main.py[co]
%attr(755,root,root) %{py_sitedir}/dbus/mainloop/pyqt5.so

%files uic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyuic5
%{py_sitedir}/PyQt5/uic
%endif

%if %{with python3}
%files -n python3-PyQt5
%defattr(644,root,root,755)
%if %{without python2}
# if not building python2 module, this plugin is built in python3 version
%dir %{_libdir}/qt5/plugins/PyQt5
%attr(755,root,root) %{_libdir}/qt5/plugins/PyQt5/libpyqt5qmlplugin.so
%endif
%dir %{py3_sitedir}/PyQt5
%attr(755,root,root) %{py3_sitedir}/PyQt5/pylupdate.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/pyrcc.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/Qt.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtBluetooth.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtCore.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtDBus.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtDesigner.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtGui.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtHelp.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtLocation.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtMultimedia.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtMultimediaWidgets.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtNetwork.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtNfc.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtOpenGL.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtPositioning.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtPrintSupport.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtQml.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtQuick.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtQuickWidgets.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSensors.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSerialPort.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSql.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSvg.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtTest.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebChannel.so
%if %{with webkit}
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebKit.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebKitWidgets.so
%endif
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebSockets.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWidgets.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtX11Extras.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtXml.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtXmlPatterns.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/_QOpenGLFunctions_2_0.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/_QOpenGLFunctions_2_1.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/_QOpenGLFunctions_4_1_Core.so
%attr(755,root,root) %{py3_sitedir}/dbus/mainloop/pyqt5.so
%{py3_sitedir}/PyQt5/QtBluetooth.pyi
%{py3_sitedir}/PyQt5/QtCore.pyi
%{py3_sitedir}/PyQt5/QtDBus.pyi
%{py3_sitedir}/PyQt5/QtDesigner.pyi
%{py3_sitedir}/PyQt5/QtGui.pyi
%{py3_sitedir}/PyQt5/QtHelp.pyi
%{py3_sitedir}/PyQt5/QtLocation.pyi
%{py3_sitedir}/PyQt5/QtMultimedia.pyi
%{py3_sitedir}/PyQt5/QtMultimediaWidgets.pyi
%{py3_sitedir}/PyQt5/QtNetwork.pyi
%{py3_sitedir}/PyQt5/QtNfc.pyi
%{py3_sitedir}/PyQt5/QtOpenGL.pyi
%{py3_sitedir}/PyQt5/QtPositioning.pyi
%{py3_sitedir}/PyQt5/QtPrintSupport.pyi
%{py3_sitedir}/PyQt5/QtQml.pyi
%{py3_sitedir}/PyQt5/QtQuick.pyi
%{py3_sitedir}/PyQt5/QtQuickWidgets.pyi
%{py3_sitedir}/PyQt5/QtSensors.pyi
%{py3_sitedir}/PyQt5/QtSerialPort.pyi
%{py3_sitedir}/PyQt5/QtSql.pyi
%{py3_sitedir}/PyQt5/QtSvg.pyi
%{py3_sitedir}/PyQt5/QtTest.pyi
%{py3_sitedir}/PyQt5/QtWebChannel.pyi
%if %{with webkit}
%{py3_sitedir}/PyQt5/QtWebKit.pyi
%{py3_sitedir}/PyQt5/QtWebKitWidgets.pyi
%endif
%{py3_sitedir}/PyQt5/QtWebSockets.pyi
%{py3_sitedir}/PyQt5/QtWidgets.pyi
%{py3_sitedir}/PyQt5/QtX11Extras.pyi
%{py3_sitedir}/PyQt5/QtXml.pyi
%{py3_sitedir}/PyQt5/QtXmlPatterns.pyi
%{py3_sitedir}/PyQt5/__init__.py
%{py3_sitedir}/PyQt5/pylupdate_main.py
%{py3_sitedir}/PyQt5/pyrcc_main.py

%files -n python3-PyQt5-uic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyuic5-3
%{py3_sitedir}/PyQt5/uic
%endif

%files devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pylupdate5
%attr(755,root,root) %{_bindir}/pyrcc5

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n sip-PyQt5
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt5

%files -n Qt5Designer-plugin-pyqt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libpyqt5.so

%files -n qscintilla2-%{module}-api
%defattr(644,root,root,755)
%{_datadir}/qt5/qsci/api/python/PyQt5.api


