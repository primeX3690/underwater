// gateway-buoy/gps_fallback.go
package main

import "fmt"

type GPSModule struct {
	LastKnownLat float64
	LastKnownLon float64
}

func (g *GPSModule) LockSurfacePosition() {
	// जब गेटवे बॉय सतह पर आता है, तो सटीक GPS लॉक प्राप्त करता है
	g.LastKnownLat = 12.9716
	g.LastKnownLon = 80.2594
	fmt.Printf("[GPS Fallback] Surface coordinates locked: Lat %.4f, Lon %.4f\n", g.LastKnownLat, g.LastKnownLon)
}