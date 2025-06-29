#
# Conditional build:
%bcond_without	qtpdf	# QtPdf bindings

%ifnarch %{x8664} aarch64
%undefine	with_qtpdf
%endif

%define		module	PyQt6
# minimal required sip version
%define		sip_ver		6.9
# last qt version covered by these bindings (minimal required is currently 5.0.0)
%define		qt_ver		%{version}

Summary:	Python bindings for the Qt6 toolkit
Summary(pl.UTF-8):	Wiązania Pythona do toolkitu Qt6
Name:		python3-%{module}
Version:	6.9.1
Release:	1
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/PyQt6/
Source0:	https://files.pythonhosted.org/packages/source/p/pyqt6/pyqt6-%{version}.tar.gz
# Source0-md5:	5ef89da9e742b75c83b0bcff05bfadb6
URL:		https://riverbankcomputing.com/software/pyqt/intro
# most of BR comes from configure.py
BuildRequires:	Qt6Bluetooth-devel >= %{qt_ver}
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Designer-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Help-devel >= %{qt_ver}
BuildRequires:	Qt6Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt6MultimediaWidgets-devel >= %{qt_ver}
BuildRequires:	Qt6Network-devel >= %{qt_ver}
BuildRequires:	Qt6Nfc-devel >= %{qt_ver}
BuildRequires:	Qt6OpenGL-devel >= %{qt_ver}
%if %{with qtpdf}
BuildRequires:	Qt6Pdf-devel >= %{qt_ver}
%endif
BuildRequires:	Qt6Positioning-devel >= %{qt_ver}
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6RemoteObjects-devel >= %{qt_ver}
BuildRequires:	Qt6Qml-devel >= %{qt_ver}
BuildRequires:	Qt6Quick-devel >= %{qt_ver}
BuildRequires:	Qt6Quick3D-devel >= %{qt_ver}
BuildRequires:	Qt6Sensors-devel >= %{qt_ver}
BuildRequires:	Qt6SerialPort-devel >= %{qt_ver}
BuildRequires:	Qt6SpatialAudio-devel >= %{qt_ver}
BuildRequires:	Qt6Sql-devel >= %{qt_ver}
BuildRequires:	Qt6Svg-devel >= %{qt_ver}
BuildRequires:	Qt6Test-devel >= %{qt_ver}
BuildRequires:	Qt6TextToSpeech-devel >= %{qt_ver}
BuildRequires:	Qt6UiTools-devel >= %{qt_ver}
BuildRequires:	Qt6WebChannel-devel >= %{qt_ver}
BuildRequires:	Qt6WebSockets-devel >= %{qt_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	Qt6Xml-devel >= %{qt_ver}
BuildRequires:	dbus-devel >= 1
BuildRequires:	pkgconfig
BuildRequires:	python3-PyQt-builder >= 1.17
BuildRequires:	python-dbus-devel >= 0.80
BuildRequires:	python3-dbus >= 0.80
BuildRequires:	python3-devel >= 1:3.6.1
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sip6 >= %{sip_ver}
Requires:	Qt6Bluetooth >= %{qt_ver}
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6DBus >= %{qt_ver}
Requires:	Qt6Designer >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Help >= %{qt_ver}
Requires:	Qt6Multimedia >= %{qt_ver}
Requires:	Qt6MultimediaWidgets >= %{qt_ver}
Requires:	Qt6Network >= %{qt_ver}
Requires:	Qt6Nfc >= %{qt_ver}
Requires:	Qt6OpenGL >= %{qt_ver}
%if %{with qtpdf}
Requires:	Qt6Pdf >= %{qt_ver}
%endif
Requires:	Qt6Positioning >= %{qt_ver}
Requires:	Qt6PrintSupport
Requires:	Qt6RemoteObjects >= %{qt_ver}
Requires:	Qt6Qml >= %{qt_ver}
Requires:	Qt6Quick >= %{qt_ver}
Requires:	Qt6Quick3D >= %{qt_ver}
Requires:	Qt6Sensors >= %{qt_ver}
Requires:	Qt6SerialPort >= %{qt_ver}
Requires:	Qt6SpatialAudio >= %{qt_ver}
Requires:	Qt6Sql >= %{qt_ver}
Requires:	Qt6Svg >= %{qt_ver}
Requires:	Qt6Test >= %{qt_ver}
Requires:	Qt6TextToSpeech >= %{qt_ver}
Requires:	Qt6UiTools >= %{qt_ver}
Requires:	Qt6WebChannel >= %{qt_ver}
Requires:	Qt6WebSockets >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	Qt6Xml >= %{qt_ver}
Requires:	python3-dbus >= 0.80
Requires:	python3-libs >= 1:3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
PyQt6 is a set of Python bindings for the Qt6 toolkit. The bindings
are implemented as a set of Python modules: Qt, QtBluetooth, QtCore,
QtDBus, QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras and QtXmlPatterns.

%description -l pl.UTF-8
PyQt6 to zbiór dowiązań do Qt6 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: Qt, QtBluetooth, QtCore, QtDBus,
QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras oraz QtXmlPatterns.

%package devel
Summary:	SIP files needed to build other bindings based on Qt6
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania innych wiązań opartych na Qt6
Group:		Development/Languages/Python
Requires:	sip6 >= %{sip_ver}
Obsoletes:	sip-PyQt6 < 6.9.0-2

%description devel
SIP files needed to build other bindings for C++ classes that inherit
from any of the Qt6 classes (e.g. KDE or your own).

%description devel -l pl.UTF-8
Pliki SIP potrzebne do budowania innych wiązań do klas C++
dziedziczących z dowolnej klasy Qt6 (np. KDE lub własnych).

%package uic
Summary:	pyuic6 development tool for Python
Summary(pl.UTF-8):	Narzędzie programistyczne pyuic6 dla Pythona
Group:		Development/Tools
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6Xml >= %{qt_ver}
Requires:	%{name} = %{version}-%{release}

%description uic
pyuic6 development tool for Python.

%description uic -l pl.UTF-8
Narzędzie programistyczne pyuic6 dla Pythona.

%package devel-tools
Summary:	PyQt6 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyQt6
Group:		Development/Tools
Requires:	python3-PyQt6 = %{version}-%{release}

%description devel-tools
PyQt6 development tools: pylupdate5, pyrcc5.

Note: this package doesn't depend on Python version.

%description devel-tools -l pl.UTF-8
Narzędzia programistyczne PyQt6: pylupdate5, pyrcc5.

Uwaga: ten pakiet nie jest zależny od wersji Pythona.

%package examples
Summary:	Examples for PyQt6
Summary(pl.UTF-8):	Przykłady do PyQt6
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description examples
Examples code demonstrating how to use the Python bindings for Qt6.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt6.

%package -n Qt6Designer-plugin-pyqt6
Summary:	Qt6 Designer plugin for Python plugins with widgets
Summary(pl.UTF-8):	Wtyczka Qt6 Designera dla wtyczek Pythona zawierających widgety
Requires:	python3-PyQt6 = %{version}-%{release}

%description -n Qt6Designer-plugin-pyqt6
This is the Qt6 Designer plugin that collects all the Python plugins
it can find as a widget collection to Designer.

%description -n Qt6Designer-plugin-pyqt6 -l pl.UTF-8
Ten pakiet zawiera wtyczkę Qt6 Designera zbierającą wszystkie wtyczki
Pythona, które jest w stanie znaleźć, jako zestaw widgetów dla
Designera.

%prep
%setup -q -n pyqt6-%{version}

grep -rl /usr/bin/env examples | xargs sed -i -e '1{
	s,^#!.*bin/env python$,#!%{__python3},
}'

%build
sip-build --build-dir build-py3 \
	--jobs %{__jobs} \
	--verbose \
	--confirm-license \
	--pep484-pyi \
	--qmake="%{_bindir}/qmake-qt6" \
	--scripts-dir=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build-py3 install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md
%dir %{_libdir}/qt6/plugins/PyQt6
%attr(755,root,root) %{_libdir}/qt6/plugins/PyQt6/libpyqt6qmlplugin.so
%dir %{py3_sitedir}/PyQt6
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtBluetooth.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtCore.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtDBus.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtDesigner.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtGui.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtHelp.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtMultimedia.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtMultimediaWidgets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtNetwork.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtNfc.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtOpenGL.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtOpenGLWidgets.abi3.so
%if %{with qtpdf}
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtPdf.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtPdfWidgets.abi3.so
%endif
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtPositioning.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtPrintSupport.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtQml.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtQuick.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtQuick3D.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtQuickWidgets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtRemoteObjects.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtSensors.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtSerialPort.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtSpatialAudio.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtSql.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtStateMachine.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtSvg.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtSvgWidgets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtTest.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtTextToSpeech.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtWebChannel.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtWebSockets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtWidgets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtXml.abi3.so
%attr(755,root,root) %{py3_sitedir}/dbus/mainloop/pyqt6.abi3.so
%{py3_sitedir}/PyQt6/__init__.py
%{py3_sitedir}/PyQt6/__pycache__
%{py3_sitedir}/pyqt6-%{version}.dist-info

# annotations (-devel?)
%{py3_sitedir}/PyQt6/QtBluetooth.pyi
%{py3_sitedir}/PyQt6/QtCore.pyi
%{py3_sitedir}/PyQt6/QtDBus.pyi
%{py3_sitedir}/PyQt6/QtDesigner.pyi
%{py3_sitedir}/PyQt6/QtGui.pyi
%{py3_sitedir}/PyQt6/QtHelp.pyi
%{py3_sitedir}/PyQt6/QtMultimedia.pyi
%{py3_sitedir}/PyQt6/QtMultimediaWidgets.pyi
%{py3_sitedir}/PyQt6/QtNetwork.pyi
%{py3_sitedir}/PyQt6/QtNfc.pyi
%{py3_sitedir}/PyQt6/QtOpenGL.pyi
%{py3_sitedir}/PyQt6/QtOpenGLWidgets.pyi
%if %{with qtpdf}
%{py3_sitedir}/PyQt6/QtPdf.pyi
%{py3_sitedir}/PyQt6/QtPdfWidgets.pyi
%endif
%{py3_sitedir}/PyQt6/QtPositioning.pyi
%{py3_sitedir}/PyQt6/QtPrintSupport.pyi
%{py3_sitedir}/PyQt6/QtQml.pyi
%{py3_sitedir}/PyQt6/QtQuick.pyi
%{py3_sitedir}/PyQt6/QtQuick3D.pyi
%{py3_sitedir}/PyQt6/QtQuickWidgets.pyi
%{py3_sitedir}/PyQt6/QtRemoteObjects.pyi
%{py3_sitedir}/PyQt6/QtSensors.pyi
%{py3_sitedir}/PyQt6/QtSerialPort.pyi
%{py3_sitedir}/PyQt6/QtSpatialAudio.pyi
%{py3_sitedir}/PyQt6/QtSql.pyi
%{py3_sitedir}/PyQt6/QtStateMachine.pyi
%{py3_sitedir}/PyQt6/QtSvg.pyi
%{py3_sitedir}/PyQt6/QtSvgWidgets.pyi
%{py3_sitedir}/PyQt6/QtTest.pyi
%{py3_sitedir}/PyQt6/QtTextToSpeech.pyi
%{py3_sitedir}/PyQt6/QtWebChannel.pyi
%{py3_sitedir}/PyQt6/QtWebSockets.pyi
%{py3_sitedir}/PyQt6/QtWidgets.pyi
%{py3_sitedir}/PyQt6/QtXml.pyi
%{py3_sitedir}/PyQt6/py.typed

%files devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt6/bindings
%{py3_sitedir}/PyQt6/sip.pyi

%files uic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyuic6
%{py3_sitedir}/PyQt6/uic

%files devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pylupdate6
%{py3_sitedir}/PyQt6/lupdate

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n Qt6Designer-plugin-pyqt6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/libpyqt6.so
