import re


class CalcIpv4:

    def __init__(self, ip, mask=None, prefix=None) -> None:
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

        self._set_broadcast()
        self._set_network()

    @property
    def network(self):
        return self._network

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def number_ip(self):
        return self._get_number_ip()

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        if not self._valid_ip(value):
            raise ValueError('invalid IP')
        self._ip = value
        self._ip_bin = self._ip_to_bin(value)

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, value):
        if not value:
            return
        if not self._valid_ip(value):
            raise ValueError('invalid Mask')
        self._mask = value
        self._mask_bin = self._ip_to_bin(value)
        if not hasattr(self, 'prefix'):
            self.prefix = self._mask_bin.count('1')

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        if not value:
            return
        if not isinstance(value, int):
            raise TypeError('Prefix must be of integer type')
        if value > 32:
            raise TypeError('Prefix must be 32 Bits')
        self._prefix = value
        self._mask_bin = (value * '1').ljust(32, '0')
        if not hasattr(self, 'mask'):
            self._mask = self._bin_to_ip(self._mask_bin)

    @staticmethod
    def _valid_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')
        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocks = ip.split('.')
        blocks_binary = [bin(int(x))[2:].zfill(8) for x in blocks]
        return ''.join(blocks_binary)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocks = [str(int(ip[i:n+i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocks)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._broadcast_bin = self._ip_bin[:self.prefix] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_network(self):
        host_bits = 32 - self.prefix
        self._network_bin = self._ip_bin[:self.prefix] + (host_bits * '0')
        self._network = self._bin_to_ip(self._network_bin)
        return self._network

    def _get_number_ip(self):
        return 2 ** (32 - self.prefix)
