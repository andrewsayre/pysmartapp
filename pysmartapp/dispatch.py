"""Defines the dispatch component for notifying others of signals."""

import asyncio
from collections import defaultdict
from typing import Any, Callable, Dict, List, Sequence

TargetType = Callable[..., Any]
DisconnectType = Callable[[], None]
ConnectType = Callable[[str, TargetType], DisconnectType]
SendType = Callable[..., Sequence[asyncio.Future]]


class Dispatcher:
    """Define the dispatch class."""

    def __init__(self, *, connect: ConnectType = None, send: SendType = None,
                 signal_prefix: str = '', loop=None):
        """Create a new instance of the dispatch component."""
        self._signal_prefix = signal_prefix
        self._signals = defaultdict(list)
        self._loop = loop or asyncio.get_event_loop()
        self._connect = connect or self._default_connect
        self._send = send or self._default_send
        self._last_sent = []

    def connect(self, signal: str, target: TargetType) \
            -> DisconnectType:
        """Connect function to signal.  Must be ran in the event loop."""
        return self._connect(self._signal_prefix + signal, target)

    def send(self, signal: str, *args: Any) -> Sequence[asyncio.Future]:
        """Fire a signal.  Must be ran in the event loop."""
        sent = self._last_sent = self._send(
            self._signal_prefix + signal, *args)
        return sent

    def _default_connect(self, signal: str, target: TargetType) \
            -> DisconnectType:
        """Connect function to signal.  Must be ran in the event loop."""
        self._signals[signal].append(target)

        def remove_dispatcher() -> None:
            """Remove signal listener."""
            try:
                self._signals[signal].remove(target)
            except ValueError:
                # signal was already removed
                pass
        return remove_dispatcher

    def _default_send(self, signal: str, *args: Any) -> \
            Sequence[asyncio.Future]:
        """Fire a signal.  Must be ran in the event loop."""
        targets = self._signals[signal]
        futures = []
        for target in targets:
            task = self._call_target(target, *args)
            futures.append(task)
        return futures

    def _call_target(self, target, *args) -> asyncio.Future:
        if asyncio.iscoroutinefunction(target):
            return self._loop.create_task(target(*args))
        return self._loop.run_in_executor(None, target, *args)

    @property
    def signals(self) -> Dict[str, List[TargetType]]:
        """Get the dictionary of registered signals and callbaks."""
        return self._signals

    @property
    def last_sent(self) -> Sequence[asyncio.Future]:
        """Get the last sent asyncio tasks."""
        return self._last_sent
