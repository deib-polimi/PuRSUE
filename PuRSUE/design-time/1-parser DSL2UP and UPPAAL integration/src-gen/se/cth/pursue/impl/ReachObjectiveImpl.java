/**
 * generated by Xtext 2.14.0
 */
package se.cth.pursue.impl;

import org.eclipse.emf.common.notify.Notification;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

import se.cth.pursue.Event;
import se.cth.pursue.PursuePackage;
import se.cth.pursue.ReachObjective;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Reach Objective</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link se.cth.pursue.impl.ReachObjectiveImpl#getGoal <em>Goal</em>}</li>
 *   <li>{@link se.cth.pursue.impl.ReachObjectiveImpl#getLife_span <em>Life span</em>}</li>
 * </ul>
 *
 * @generated
 */
public class ReachObjectiveImpl extends MinimalEObjectImpl.Container implements ReachObjective
{
  /**
   * The cached value of the '{@link #getGoal() <em>Goal</em>}' reference.
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @see #getGoal()
   * @generated
   * @ordered
   */
  protected Event goal;

  /**
   * The default value of the '{@link #getLife_span() <em>Life span</em>}' attribute.
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @see #getLife_span()
   * @generated
   * @ordered
   */
  protected static final int LIFE_SPAN_EDEFAULT = 0;

  /**
   * The cached value of the '{@link #getLife_span() <em>Life span</em>}' attribute.
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @see #getLife_span()
   * @generated
   * @ordered
   */
  protected int life_span = LIFE_SPAN_EDEFAULT;

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  protected ReachObjectiveImpl()
  {
    super();
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  @Override
  protected EClass eStaticClass()
  {
    return PursuePackage.Literals.REACH_OBJECTIVE;
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  public Event getGoal()
  {
    if (goal != null && goal.eIsProxy())
    {
      InternalEObject oldGoal = (InternalEObject)goal;
      goal = (Event)eResolveProxy(oldGoal);
      if (goal != oldGoal)
      {
        if (eNotificationRequired())
          eNotify(new ENotificationImpl(this, Notification.RESOLVE, PursuePackage.REACH_OBJECTIVE__GOAL, oldGoal, goal));
      }
    }
    return goal;
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  public Event basicGetGoal()
  {
    return goal;
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  public void setGoal(Event newGoal)
  {
    Event oldGoal = goal;
    goal = newGoal;
    if (eNotificationRequired())
      eNotify(new ENotificationImpl(this, Notification.SET, PursuePackage.REACH_OBJECTIVE__GOAL, oldGoal, goal));
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  public int getLife_span()
  {
    return life_span;
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  public void setLife_span(int newLife_span)
  {
    int oldLife_span = life_span;
    life_span = newLife_span;
    if (eNotificationRequired())
      eNotify(new ENotificationImpl(this, Notification.SET, PursuePackage.REACH_OBJECTIVE__LIFE_SPAN, oldLife_span, life_span));
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  @Override
  public Object eGet(int featureID, boolean resolve, boolean coreType)
  {
    switch (featureID)
    {
      case PursuePackage.REACH_OBJECTIVE__GOAL:
        if (resolve) return getGoal();
        return basicGetGoal();
      case PursuePackage.REACH_OBJECTIVE__LIFE_SPAN:
        return getLife_span();
    }
    return super.eGet(featureID, resolve, coreType);
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  @Override
  public void eSet(int featureID, Object newValue)
  {
    switch (featureID)
    {
      case PursuePackage.REACH_OBJECTIVE__GOAL:
        setGoal((Event)newValue);
        return;
      case PursuePackage.REACH_OBJECTIVE__LIFE_SPAN:
        setLife_span((Integer)newValue);
        return;
    }
    super.eSet(featureID, newValue);
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  @Override
  public void eUnset(int featureID)
  {
    switch (featureID)
    {
      case PursuePackage.REACH_OBJECTIVE__GOAL:
        setGoal((Event)null);
        return;
      case PursuePackage.REACH_OBJECTIVE__LIFE_SPAN:
        setLife_span(LIFE_SPAN_EDEFAULT);
        return;
    }
    super.eUnset(featureID);
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  @Override
  public boolean eIsSet(int featureID)
  {
    switch (featureID)
    {
      case PursuePackage.REACH_OBJECTIVE__GOAL:
        return goal != null;
      case PursuePackage.REACH_OBJECTIVE__LIFE_SPAN:
        return life_span != LIFE_SPAN_EDEFAULT;
    }
    return super.eIsSet(featureID);
  }

  /**
   * <!-- begin-user-doc -->
   * <!-- end-user-doc -->
   * @generated
   */
  @Override
  public String toString()
  {
    if (eIsProxy()) return super.toString();

    StringBuilder result = new StringBuilder(super.toString());
    result.append(" (life_span: ");
    result.append(life_span);
    result.append(')');
    return result.toString();
  }

} //ReachObjectiveImpl
