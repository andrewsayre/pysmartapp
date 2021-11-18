# pysmartapp
[![CI Status](https://github.com/andrewsayre/pysmartapp/workflows/CI/badge.svg)](https://github.com/andrewsayre/pysmartapp/actions)
[![codecov](https://codecov.io/gh/andrewsayre/pysmartapp/branch/master/graph/badge.svg?token=VKPQ25JRAY)](https://codecov.io/gh/andrewsayre/pysmartapp)
[![image](https://img.shields.io/pypi/v/pysmartapp.svg)](https://pypi.org/project/pysmartapp/)
[![image](https://img.shields.io/pypi/pyversions/pysmartapp.svg)](https://pypi.org/project/pysmartapp/)
[![image](https://img.shields.io/pypi/l/pysmartapp.svg)](https://pypi.org/project/pysmartapp/)

A python implementation of the WebHook-based [SmartThings SmartApp](https://smartthings.developer.samsung.com/develop/guides/smartapps/basics.html) that uses asyncio and the dispatcher pattern to notify callbacks (coroutines or functions) of SmartApp lifecycle events.