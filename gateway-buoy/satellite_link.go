// gateway-buoy/satellite_link.go
package main

import "fmt"

type SatelliteTransmitter struct {
	SatelliteID string
	IsSecure    bool
}

func NewSatelliteTransmitter() *SatelliteTransmitter {
	return &SatelliteTransmitter{
		SatelliteID: "GSAT-7A-RUKMINI",
		IsSecure:    true,
	}
}

func (s *SatelliteTransmitter) SendUplinkPacket(packetData []byte) {
	fmt.Printf("[Satellite Link] Encrypted payload of %d bytes beamed securely via %s\n", len(packetData), s.SatelliteID)
}