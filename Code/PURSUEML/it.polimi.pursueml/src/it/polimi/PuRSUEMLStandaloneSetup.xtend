/*
 * generated by Xtext 2.17.0.M1
 */
package it.polimi


/**
 * Initialization support for running Xtext languages without Equinox extension registry.
 */
class PuRSUEMLStandaloneSetup extends PuRSUEMLStandaloneSetupGenerated {

	def static void doSetup() {
		new PuRSUEMLStandaloneSetup().createInjectorAndDoEMFRegistration()
	}
}
